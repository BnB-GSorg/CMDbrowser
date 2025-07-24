import telnetlib

CHUNK_SIZE = 1024

def download_chunks(host, port, base_filename, total_chunks):
    tn = telnetlib.Telnet(host, port)
    tn.read_until(b"Send CHUNK_ID")
    for i in range(total_chunks):
        tn.write(f"{i}\n".encode())
        chunk = tn.read_until(b"CHUNK_NOT_FOUND", timeout=2)
        if b"CHUNK_NOT_FOUND" in chunk or b"ERROR" in chunk:
            print(f"Chunk {i} not found.")
            continue
        # Save chunk
        with open(f"{base_filename}.chunk{i}", 'wb') as cf:
            cf.write(chunk)
        print(f"Downloaded chunk {i}")
    tn.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 5:
        print("Usage: python telnet_file_client.py [host] [port] [base_filename] [total_chunks]")
        exit(1)
    host = sys.argv[1]
    port = int(sys.argv[2])
    base_filename = sys.argv[3]
    total_chunks = int(sys.argv[4])
    download_chunks(host, port, base_filename, total_chunks)