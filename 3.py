def append_text_to_file(filename, text):
    try:
        with open(filename, 'a') as file:
            file.write(text + '\n')
        print("Text appended to the file successfully.")
    except Exception as e:
        print("An error occurred:", str(e))

def display_file_contents(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("Contents of the file:")
            print(contents)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", str(e))

filename = "3.txt"
text_to_append = input("Enter text to append to the file: ")

append_text_to_file(filename, text_to_append)

display_file_contents(filename)