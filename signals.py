import pandas as pd

df = pd.read_csv("brk_-_b_data.csv", index_col=0, parse_dates=True)
print(df)
short_window = 20
long_window = 100