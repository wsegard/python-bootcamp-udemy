import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('College_data.csv', index_col=0)
#print(data.info())
print(data.head())

#sns.scatterplot(x=data['Grad.Rate'], y=data['Room.Board'], hue=data['Private'])
#plt.show()

sns.set_style('darkgrid')
g = sns.FacetGrid(data,hue="Private",palette='coolwarm',height=6,aspect=2)
g = g.map(plt.hist,'Grad.Rate',bins=20,alpha=0.7)
plt.show()

print(data[data['Grad.Rate'] > 100])
data['Grad.Rate']['Cazenovia College'] = 100


