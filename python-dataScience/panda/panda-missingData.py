import pandas as pd
import numpy as np

df = pd.DataFrame({'A':[1,2,np.nan],
                  'B':[5,np.nan,np.nan],
                  'C':[1,2,3]})

#print(df)

#print(df.dropna())
print(df)
#print(df.dropna(axis=1))
#print(df.dropna(thresh=1))
#********* Keep only the rows with at least 2 non-NA values
#print(df.dropna(thresh=2))
#print(df.dropna(thresh=3))

print(df.fillna(value='FILL VALUE'))
print(df['A'].fillna(value=df['A'].mean()))
