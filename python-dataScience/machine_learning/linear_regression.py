import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

USAhousing = pd.read_csv('USA_Housing.csv')
print(USAhousing.head())
print("***************************** \n")
print(USAhousing.info())
print("***************************** \n")
print(USAhousing.describe())
print("***************************** \n")
print(USAhousing.columns)


#sns.pairplot(USAhousing)
#plt.tight_layout()
#plt.show()

#sns.distplot(USAhousing['Price'])
#plt.tight_layout()
#plt.show()


#sns.heatmap(USAhousing.corr())
#plt.tight_layout()
#plt.show()

X = USAhousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
               'Avg. Area Number of Bedrooms', 'Area Population']]
y = USAhousing['Price']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

#print(type(USAhousing))
#print(type(X))
#print(X_train.info())

from sklearn.linear_model import LinearRegression

lm = LinearRegression(normalize=True)
lm.fit(X_train,y_train)
print(lm.fit(X_train,y_train))
print("***************************** \n")
print(lm.intercept_)
print("***************************** \n")
coeff_df = pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient'])
print(coeff_df)
print("***************************** \n")
predictions = lm.predict(X_test)
#plt.scatter(y_test,predictions, s=20)
sns.distplot((y_test-predictions),bins=50)
plt.show()

from sklearn import metrics

print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))



