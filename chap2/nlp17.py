import pandas as pd 

df = pd.read_csv('chap2/popular-names.txt', sep='\t', header=None)
# df[0].unique().to_csv('chap2/ans17.txt', sep='\t', index=False, header=None)
print(df[0].unique(), len(df[0].unique()))