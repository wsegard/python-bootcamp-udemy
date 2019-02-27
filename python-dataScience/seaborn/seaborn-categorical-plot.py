import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
#print(tips.head())

#sns.barplot(x='sex',y='total_bill',data=tips)


import numpy as np
#sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)

#sns.countplot(x='sex',data=tips)

#sns.boxplot(x="day", y="total_bill", data=tips,palette='rainbow')

sns.boxplot(data=tips,palette='rainbow',orient='h')

plt.show()

