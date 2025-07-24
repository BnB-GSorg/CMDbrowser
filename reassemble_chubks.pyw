from chunk_utils import reassemble_file

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python reassemble_chunks.py [base_filename] [total_chunks] [output_filename]")
        exit(1)
    base_filename = sys.argv[1]
    total_chunks = int(sys.argv[2])
    output_filename = sys.argv[3]
    reassemble_file(base_filename, total_chunks, output_filename)
    print(f"File reassembled as {output_filename}")