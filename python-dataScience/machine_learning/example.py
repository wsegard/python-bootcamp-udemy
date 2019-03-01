import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('example.csv')
print(data.head())
print("***************************** \n")
print(data.info())
print("***************************** \n")
print(data.describe())
print("***************************** \n")
print(data.columns)


X = data[['x']]
y = data[['y']]
print(X.info())
print(y.info())

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=40)

from sklearn.linear_model import LinearRegression

lm = LinearRegression(normalize=True)
lm.fit(X_train,y_train)
print("***************************** \n")
print(lm.intercept_)
print("***************************** \n")
coeff_df = pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient'])
print(coeff_df)
print("***************************** \n")
predictions = lm.predict(X_test)
sns.distplot((y_test-predictions),bins=50)
plt.show()

from sklearn import metrics

print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))
