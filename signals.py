import pandas as pd

df = pd.read_csv("brk_-_b_data.csv", index_col=0, parse_dates=True)
short_window = 20
long_window = 100

#Розрахунок ковзних за допомогою .rolling().mean()

df["MA_short"] = df["Close"].rolling(window=short_window).mean()
df["MA_long"] = df["Close"].rolling(window=long_window).mean()

df["Position"] = 0
df.loc[df["MA_short"] > df["MA_long"], "Position"] = 1

df = df.dropna(subset=["MA_long"]).copy()
print(df)