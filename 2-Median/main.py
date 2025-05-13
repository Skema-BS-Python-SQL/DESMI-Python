# Use the NumPy median() method to find the middle value:
import numpy

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

print("speed list: " + str(speed))

x = numpy.median(speed)

print("Median: " + str(x))

# If there are two numbers in the middle, divide the sum of those numbers by two.

speed = [99, 86, 87, 88, 86, 103, 87, 94, 78, 77, 85, 86]

print("speed list (with two numbers in the middle): " + str(speed))

x = numpy.median(speed)

print("Median :" + str(x))
