def greet():
    print("Hello, World!")

#greet()

def add(x, y):
  return x + y

result = add(3, 4)
#print(result)  # Output: 7


# Define a function to add two numbers
def add_numbers(num1, num2):
    sum_result = num1 + num2
    return sum_result

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Call the function and print the result
result = add_numbers(num1, num2)
print("Sum:", result)