import pandas as pd

df = pd.read_csv('stkindex.csv',index_col=['Unnamed: 0'])
print(df.iloc[0:5,0:5])
