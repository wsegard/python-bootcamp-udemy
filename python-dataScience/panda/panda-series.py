import numpy as np
import pandas as pd


labels = ['a','b','c']
my_list = [10,20,30]
arr = np.array([10,20,30])
d = {'a':10,'b':20,'c':30}

#print(pd.Series(data=my_list))
#print(pd.Series(data=my_list,index=labels))
#print(pd.Series(my_list,labels))

#print(pd.Series(arr))
#print(pd.Series(arr,labels))

#print(pd.Series(d))

#print(pd.Series(data=labels))

#print(pd.Series([sum,print,len]))

ser1 = pd.Series([1,2,3,4],index = ['USA', 'Germany','USSR', 'Japan'])
#print(ser1)
ser2 = pd.Series([1,2,5,4],index = ['USA', 'Germany','Italy', 'Japan'])
#print(ser2)

#print(ser1['USA'])

print(ser1 + ser2)
