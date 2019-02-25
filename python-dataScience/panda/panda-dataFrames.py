import pandas as pd
import numpy as np

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
#print(df)

#print(df['W'])
#print(df[['W','Z']])
#print(df.W)
#print(type(df['W']))

df['new'] = df['W'] + df['Y']
#print(df)

#print(df.drop('new',axis=1))
df.drop('new',axis=1)
#print(df)

df.drop('new',axis=1,inplace=True)
#print(df)

#print(df.drop('E',axis=0))

#print(df.loc['A'])
#print(df.iloc[2])
#print(df.loc['B','Y'])
#print(df.loc[['A','B'],['W','Y']])
#print(df>0)
#print(df[df > 0])
#print(df[df['W']>0])
#print(df[df['W']>0]['Y'])
#print(df[df['W']>0][['Y','X']])
#print(df[(df['W']>0) & (df['Y'] > 1)])
df.reset_index()
#print(df)
#print(df.reset_index())
newind = 'CA NY WY OR CO'.split()
df['States'] = newind
#print(df)
df.set_index('States')
#print(df.set_index('States'))
#print(df)
df.set_index('States',inplace=True)
#print(df)
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
#print(hier_index)
df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
#print(df)
#print(df.loc['G1'])
#print(df.loc['G1'].loc[1])

df.index.names = ['Group','Num']
print(df)
print(df.xs('G1'))
print(df.xs(['G1',1]))
print(df.xs(1,level='Num'))
