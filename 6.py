def read_file_lines(filename):
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            lines.append(line.strip())
    return lines

filename = '4.txt'
lines = read_file_lines(filename)
print("Contents of the file stored in a list:")
for line in lines:
    print(line)
