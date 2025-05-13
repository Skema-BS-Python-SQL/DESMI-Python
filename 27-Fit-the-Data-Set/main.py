# Fit the Data Set
# What does the data set look like? 
# In my opinion I think the best fit would be 
# a polynomial regression, so let us draw a line 
# of polynomial regression.
import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

myline = numpy.linspace(0, 6, 100)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
#plt.show()
plt.savefig('Fit_set.png')
# the line indicates that a customer 
# spending 6 minutes in the shop 
# would make a purchase worth 200. 
# That is probably a sign of overfitting.