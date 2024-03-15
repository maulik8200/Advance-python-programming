def get_odd_number():
    while True:
        try:
            number = int(input("Please enter an odd number: "))
            if number % 2 != 0:
                return number
            else:
                raise ValueError("You must enter an odd number.")
        except ValueError as ve:
            print(ve)

try:
    odd_number = get_odd_number()
    print("You entered:", odd_number)
except KeyboardInterrupt:
    print("\nProgram terminated by the user.")