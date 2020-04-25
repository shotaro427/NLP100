import pandas as pd 

df = pd.read_csv('chap2/popular-names.txt', sep='\t', header=None)
df_s = df.sort_values(2, ascending=False)
print(df_s)