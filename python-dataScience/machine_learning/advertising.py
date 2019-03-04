import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

ad_data = pd.read_csv('advertising.csv')
print(ad_data.head())
print("\n**********************\n")
print(ad_data.info())
print("\n**********************\n")
print(ad_data.describe())

#ad_data['Age'].hist(color='blue',bins=40,figsize=(8,4))
#sns.jointplot(ad_data['Age'],ad_data['Area Income'])
#sns.jointplot(x='Age', y='Area Income', data=ad_data)
#sns.jointplot(x='Age', y='Daily Time Spent on Site', data=ad_data, kind='kde', color='red')
#sns.jointplot(x='Daily Time Spent on Site', y='Daily Internet Usage', data=ad_data, color='green')
#sns.pairplot(ad_data, hue='Clicked on Ad')
#plt.show()

from sklearn.model_selection import train_test_split

X = ad_data[['Daily Time Spent on Site', 'Age', 'Area Income','Daily Internet Usage', 'Male']]
y = ad_data['Clicked on Ad']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

from sklearn.linear_model import LogisticRegression

logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)
predictions = logmodel.predict(X_test)

from sklearn.metrics import classification_report
print(classification_report(y_test,predictions))
