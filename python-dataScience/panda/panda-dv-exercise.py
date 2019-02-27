
import pandas as pd
import matplotlib.pyplot as plt
df3 = pd.read_csv('df3.csv')
plt.style.use('ggplot')
#print(df3.info())
#df3.plot.scatter(x='a',y='b',c='red',s=30,figsize=(12,3))
#df3['a'].plot.hist()
df3['a'].plot.hist(alpha=0.5,bins=25)

plt.show()
