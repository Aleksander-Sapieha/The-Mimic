import sys

def interpret_from_file(file_path):
    with open(file_path, 'r') as file:
        code = file.read()
    return code

def main():
    if len(sys.argv) != 2:
        print("Usage: ./mimic.exe <filename>")
        sys.exit(1)
    filepath = sys.argv[1]
    try:
        result = interpret_from_file(filepath)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
