def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("An error occurred:", e)

file_path = '2.txt'
read_text_file(file_path)
