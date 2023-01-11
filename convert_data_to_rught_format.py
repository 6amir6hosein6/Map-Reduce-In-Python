import pandas as pd

df = pd.read_excel('sport.xlsx', sheet_name='Sheet1')
print(df)
with open('sport.txt','w') as outfile:
    df.to_string(outfile, index=False)
