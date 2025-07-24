import os

CHUNK_SIZE = 1024

def split_file(filename):
    """Splits a file into chunks and saves them as separate files."""
    with open(filename, 'rb') as f:
        i = 0
        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            chunk_filename = f"{filename}.chunk{i}"
            with open(chunk_filename, 'wb') as cf:
                cf.write(chunk)
            i += 1
    return i  # number of chunks

def reassemble_file(base_filename, total_chunks, output_filename):
    """Reassembles chunks into the original file."""
    with open(output_filename, 'wb') as of:
        for i in range(total_chunks):
            chunk_filename = f"{base_filename}.chunk{i}"
            with open(chunk_filename, 'rb') as cf:
                of.write(cf.read())