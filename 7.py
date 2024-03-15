def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            content = ''.join(lines)
        return content
    except FileNotFoundError:
        print("File not found.")
        return None

file_path = '4.txt'
file_content = read_file(file_path)

if file_content is not None:
    print("File content:")
    print(file_content)
