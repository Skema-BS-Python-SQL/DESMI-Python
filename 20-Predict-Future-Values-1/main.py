# Multiple Regression using data from CSV
#
import pandas
from sklearn import linear_model
# The Pandas module allows us to read csv files 
# and return a DataFrame object.
df = pandas.read_csv("data.csv")
# Then make a list of the independent values 
# and call this variable X.
# Put the dependent values in a variable called y.
# 
# It is common to name the list of independent values with 
# a upper case X, and the list of dependent values 
# with a lower case y
X = df[['Weight', 'Volume']]
y = df['CO2']

# From the sklearn module we will use the 
# LinearRegression() method to create a linear regression object.
#
# This object has a method called fit() 
# that takes the independent and dependent values as parameters 
# and fills the regression object 
# with data that describes the relationship
regr = linear_model.LinearRegression()
regr.fit(X, y)

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2) # result is [107.2087328]
# We have predicted that a car with 1.3 liter engine, 
# and a weight of 2300 kg, will release approximately 
# 107 grams of CO2 for every kilometer it drives

