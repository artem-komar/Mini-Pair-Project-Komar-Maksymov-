import pandas as pd
df=pd.read_csv("trading_signals.csv", index_col=0, parse_dates=True)

start_capital=10000.0

df["Market_Return"] = df["Close"].pct_change()
df["Strategy_Return"] = df["Market_Return"]*df["Position"].shift(1)