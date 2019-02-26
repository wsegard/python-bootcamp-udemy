import pandas as pd
import numpy as np

df = pd.read_csv('example.csv')
#print(df)
#df.to_csv('example',index=False)

df2 = pd.read_excel('Excel_Sample.xlsx',sheet_name='Sheet1')
#print(df2)
#df.to_excel('Excel_Sample.xlsx',sheet_name='Sheet1')

df3 = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
#print(df3[0])

from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')
df.to_sql('data', engine)
sql_df = pd.read_sql('data',con=engine)
print(sql_df)
