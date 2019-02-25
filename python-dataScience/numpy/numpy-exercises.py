import numpy as np

#arr0 = np.zeros(10)
#print(arr0)
#arr1 = np.ones(10)
#print(arr1)
#arr5 = 5 * np.ones(10)
#print(arr5)
#print(np.arange(10,51))
#print(np.arange(10,51,2))
#arr = np.arange(10,51,2)
#print(arr[arr%2 == 0])

#arr = np.arange(0,9)
#print(arr.reshape(3,3))
#print(np.eye(3))
#print(np.random.rand(1))
#print(np.random.randn(25))

#arr = np.arange(0.01,1.01,0.01)
#print(arr.reshape(10,10))

#arr = np.linspace(0,1,20)
#print(arr)

mat = np.arange(1,26).reshape(5,5)
#print(mat[2:,1:])
#print(mat[3,4])
print(mat[:3,1].shape)
print(mat[:3,1:2].shape)
#print(mat[4])
#print(mat[3:])

print(mat.sum())
print(mat.std())
print(mat.sum(axis=0))
print(mat.sum(axis=1))
