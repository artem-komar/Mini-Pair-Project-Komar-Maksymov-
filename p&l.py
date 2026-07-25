import pandas as pd
df=pd.read_csv("trading_signals.csv", index_col=0, parse_dates=True)

start_capital=10000.0

df["Market_Return"] = df["Close"].pct_change()
df["Strategy_Return"] = df["Market_Return"]*df["Position"].shift(1)

market_growth_factor= 1 + df["Market_Return"]
strategy_growth_factor= 1 + df["Strategy_Return"]
df["Cum_Market_Return"]= market_growth_factor.cumprod()- 1
df["Cum_Strategy_Return"]= strategy_growth_factor.cumprod()- 1
df["Portfolio_Value"]=(start_capital *(1+df["Cum_Strategy_Return"])).round(2)