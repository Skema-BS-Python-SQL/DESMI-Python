n1 = 20.5 + 10.2
n2 = 20.5 - 10.2
n3 = 20.5 * 10.2
# The division of two integers always returns a float
n4 = 20 / 10
print(str(n1) + "\n" + str(n2) + "\n" + str(n3) + "\n" + str(n4))
#If you mix an integer and a float
# in any arithmetic operation, the result is a float
n5 = 1 + 2.0
print(n5)
# Due to the internal representation of floats, 
# Python will try to represent the result as precisely as possible.
# However, you may get the result that you would not expect
n6 = 0.1 + 0.2
print(n6)