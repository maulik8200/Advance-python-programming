def read_last_n_lines(file_path, n):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            last_n_lines = lines[-n:]
            return last_n_lines
    except FileNotFoundError:
        return f"File '{file_path}' not found."
    except Exception as e:
        return f"Error occurred: {str(e)}"

def main():
    file_path = input("Enter the path of the file: ")
    n = int(input("Enter the number of last lines to read: "))

    last_n_lines = read_last_n_lines(file_path, n)
    if isinstance(last_n_lines, list):
        print(f"Last {n} lines of the file '{file_path}':")
        for line in last_n_lines:
            print(line.strip())
    else:
        print(last_n_lines)

if __name__ == "__main__":
    main()
