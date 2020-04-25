import pandas as pd 

df = pd.read_csv('chap2/popular-names.txt', sep='\t', header=None)
df[0].to_csv('chap2/col1.txt', index=False, header=None)
df[1].to_csv('chap2/col2.txt', index=False, header=None)
