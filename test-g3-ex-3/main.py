#num1 = float(input("Enter the first number: "))
#num2 = float(input("Enter the second number: "))
#print("Sum:", num1 + num2)
#print("Difference:", num1 - num2)
#print("Product:", num1 * num2)
#print("Quotient:", num1 / num2)
#------
# Take two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display their sum
print("Sum:", num1 + num2)

# Display their difference
print("Difference:", num1 - num2)

# Display their product
print("Product:", num1 * num2)

# Check for division by zero before attempting to divide
if num2 == 0:
    print("Quotient: Division by zero is not allowed!")
else:
    print("Quotient:", num1 / num2)
