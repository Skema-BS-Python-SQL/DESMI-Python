#7: Conditional Statements
#
# Ask the user for their age
age = int(input("Please enter your age: "))

# Check the age group and print a message accordingly
if age <= 12:
    print("You are a child.")
elif age <= 17:
    print("You are a teenager.")
elif age <= 64:
    print("You are an adult.")
else:
    print("You are a senior.")