# We will Python module Matplotlib to draw a histogram.
# Note: The array values are random numbers 
# and will not show the exact same result on each run
import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 250)

#print(x)

plt.hist(x, 5)
# plt.show() 
# show not work on replit.com
# you have to create a file and click it
# <-- to open it from Files list
plt.savefig('histogram01.png')
