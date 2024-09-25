import pandas as pd

df = pd.read_csv('examples/Fixed.csv')
df = df.sort_values(by='%CPU', ascending=False)
df.to_csv('examples/PSAUX_sorted.csv', index=False)