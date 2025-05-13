# Start with a data set you want to test.
# The x-axis represents the number 
# of minutes before making a purchase.
# The y-axis represents the amount of money 
# spent on the purchase.
import numpy
import matplotlib.pyplot as plt

numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

plt.scatter(x, y)
# plt.show()
plt.savefig('data_set.png')