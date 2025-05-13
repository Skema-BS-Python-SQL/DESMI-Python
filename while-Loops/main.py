# Simple while loop
while True:
    choice = input("Do you want to continue? (yes/no): ")

    if choice.lower() == "no":
        print("Exiting the loop.")
        break
    elif choice.lower() == "yes":
        print("Continuing...")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")