import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')

titanic = sns.load_dataset('titanic')

#sns.jointplot(x='fare',y='age',data=titanic,kind='scatter',xlim=[-30, 600])
#sns.distplot(titanic['fare'], kde=False)
#sns.boxplot(x="class", y="age", data=titanic,palette='rainbow')
#sns.swarmplot(x="class", y="age", data=titanic)
#sns.countplot(x='sex',data=titanic)
#sns.heatmap(titanic.corr(),cmap='coolwarm')

g = sns.FacetGrid(data=titanic,col='sex')
g.map(plt.hist,'age')

plt.show()
