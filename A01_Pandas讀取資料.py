import pandas as pd

df = pd.read_excel('./02_Data/植生指標萃取結果範例.xlsx')
print(df)

dt_filter = (df['N_type']=='N3') & (df['W_type']=="CP")
dt = df[dt_filter]
print(dt)
