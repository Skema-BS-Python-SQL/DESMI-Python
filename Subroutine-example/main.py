#Example1 of a Function returning a value
def addNum(num1, num2):
    total = num1 + num2
    return (total)

num1 = int(input("Please enter a number to be added: "))
num2 = int(input("Please enter another number to be added: "))
answer = addNum(num1, num2)
print (answer)