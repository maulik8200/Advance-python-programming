def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        print("File not found!")
        return -1

file_path = '4.txt'
lines = count_lines(file_path)
if lines != -1:
    print(f"Number of lines in the file: {lines}")
