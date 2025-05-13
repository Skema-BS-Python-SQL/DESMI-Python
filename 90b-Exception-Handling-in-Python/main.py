#9.0b Exception Handling in Python
while True:
    try:
        user_input = input("Enter a number (or 'q' to quit): ")

        if user_input.lower() == 'q':
            print("Quitting the program.")
            break

        number = int(user_input)
        print(f"You entered: {number}")

        result = 10 / number
        print(f"Result of 10 / {number} = {result}")
    except ValueError:
        print("That's not a valid number!")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")