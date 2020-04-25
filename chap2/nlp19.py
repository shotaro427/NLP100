import pandas as pd 

df = pd.read_csv('chap2/popular-names.txt', sep='\t', header=None)
df_u = df[0].value_counts()
print(df_u)