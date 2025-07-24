import telnetlib
import socket
import threading
import os

CHUNK_SIZE = 1024

def handle_client(conn, addr, base_filename):
    conn.sendall(b"Welcome to the Telnet File Server!\n")
    conn.sendall(b"Send CHUNK_ID (e.g. 0, 1, 2, ...):\n")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        try:
            chunk_id = int(data.decode().strip())
            chunk_filename = f"{base_filename}.chunk{chunk_id}"
            if os.path.exists(chunk_filename):
                with open(chunk_filename, 'rb') as cf:
                    conn.sendall(cf.read())
            else:
                conn.sendall(b"CHUNK_NOT_FOUND")
        except Exception as e:
            conn.sendall(b"ERROR")
    conn.close()

def start_server(host, port, base_filename):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    print(f"Telnet File Server listening on {host}:{port}")
    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle_client, args=(conn, addr, base_filename)).start()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python telnet_file_server.py [host] [port] [base_filename]")
        exit(1)
    host = sys.argv[1]
    port = int(sys.argv[2])
    base_filename = sys.argv[3]
    start_server(host, port, base_filename)