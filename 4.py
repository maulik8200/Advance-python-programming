def read_first_n_lines(file_name, n):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines[:n]:
                print(line.strip())
    except FileNotFoundError:
        print("File not found!")

file_name = "4.txt"
n = 5
read_first_n_lines(file_name, n)