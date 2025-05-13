# A typical normal data distribution
#
# We use the array with 100000 values,
# to draw a histogram with 100 bars.
# We specify that the mean value is 5.0,
# and the standard deviation is 1.0.
# Meaning that the values should be concentrated around 5.0,
# and rarely further away than 1.0 from the mean.
#
import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
# plt.show()
plt.savefig('NormalDataDis01.png')
# And as you can see from the histogram, most values are between 4.0 and 6.0, with a top at approximately 5.0.
