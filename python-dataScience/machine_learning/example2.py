import numpy as np
#from numpy import random

X = np.zeros((100,2))
X[:,0] = 1

m = len(X)
n = len(X[0])



for i in range(0,m):
  X[i,1] = i

y = np.zeros(m)

for i in range(0,m):
  y[i] = 2 * X[i,1] + 3 + np.random.randn()

theta = np.random.rand(2)
print(theta)

alpha = 0.01

for i in range(0,1000):
  prediction = np.dot(X,theta)
  error = prediction - y
  theta = theta - (alpha * (1/m) * np.dot(X.T,error))

print(theta)
