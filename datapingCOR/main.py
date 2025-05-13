# https://matplotlib.org/1.3.1/users/recipes.html#fixing-common-date-annoyances
#
import pandas as pd
import chart_studio.plotly as px

df = pd.read_csv('cor.csv', sep=';')

#SECONDS
fig = px.line(df, x='DATE', y='TRIES', title='')
fig.show()