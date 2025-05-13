# Print the coefficient values of the regression object
#
# In this case, we can ask for the coefficient value of weight
# against CO2, and for volume against CO2. 
# The answers we get tells us what would happen 
# if we increase, or decrease, one of the independent values.
import pandas
from sklearn import linear_model

df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

print(regr.coef_) # result [0.00755095 0.00780526]
#
# The result array represents the coefficient values 
# of weight and volume.
# Weight: 0.00755095
# Volume: 0.00780526
#
# These values tell us that if the weight increase by 1kg, 
# the CO2 emission increases by 0.00755095g.
# And if the engine size (Volume) increases by 1 cm3, 
# the CO2 emission increases by 0.00780526 g.

# TODO : use the same example from before, 
# but change the weight from 2300 to 3300: