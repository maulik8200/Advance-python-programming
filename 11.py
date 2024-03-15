def write_list_to_file(lst, filename):
    with open(filename, 'w') as file:
        for item in lst:
            file.write(str(item) + '\n')

my_list = [1, 2, 3, 4, 5]
file_name = 'list_output.txt'
write_list_to_file(my_list, file_name)
print(f"List has been written to '{file_name}'.")