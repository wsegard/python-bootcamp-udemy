import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
#plt.style.use('bmh')
#plt.style.use('dark_background')
#plt.style.use('fivethirtyeight')

df1 = pd.read_csv('df1.csv')
df2 = pd.read_csv('df2.csv')

#print(df1.info())
#print(df1.index)

#df1['A'].hist()
#plt.show()

#df2.plot.area(alpha=0.4)
#df2.plot.bar()
#df2.plot.bar(stacked=True)
#df1['A'].plot.hist(bins=50)
#df1.plot.line(x='Dates', y='A',figsize=(12,3),lw=1)
#df1.plot.scatter(x='A',y='B')
#df1.plot.scatter(x='A',y='B',c='C',cmap='coolwarm')
df1.plot.scatter(x='A',y='B',s=df1['C']*200)


plt.show()
