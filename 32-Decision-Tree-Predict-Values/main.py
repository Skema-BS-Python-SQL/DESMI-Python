# Should I go see a show starring a
# 40 years old American comedian,
# with 10 years of experience,
# and a comedy ranking of 7?
import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

df = pandas.read_csv("data.csv")

d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

features = ['Age', 'Experience', 'Rank', 'Nationality']
X = df[features]
y = df['Go']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

print(str(dtree.predict([[40, 10, 7, 1]])) +
      " : comedy ranking of 7")  # comedy ranking of 7

# What would the answer be if the comedy rank was 6?
print(str(dtree.predict([[40, 10, 6, 1]])) +
      " : comedy ranking of 6")  # comedy ranking of 6

print("[1] means 'GO'")
print("[0] means 'NO'")

# You will see that the Decision Tree gives you different
# results if you run it enough times, even if you feed it with the same data.
# That is because the Decision Tree does not give us a 100% certain answer.
# It is based on the probability of an outcome, and the answer will vary.
