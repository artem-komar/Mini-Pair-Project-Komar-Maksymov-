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

total_market_return= df["Cum_Market_Return"].iloc[-1]* 100
total_strategy_return= df["Cum_Strategy_Return"].iloc[-1]* 100
final_balance= df["Portfolio_Value"].iloc[-1]
net_profit= final_balance -start_capital
total_trades=sum(df["Signal"]=="Buy")

print(f"Початковий депозит: ${round(start_capital, 2)}")
print(f"Кінцевий баланс: ${round(final_balance, 2)}")
print(f"Абсолютний прибуток/збиток: ${round(net_profit, 2)}")
print(f"Дохідність стратегії: {round(total_strategy_return, 2)}%")
print(f"Дохідність ринку(Buy & Hold): {round(total_market_return, 2)}%")
print(f"Кількість угод(Buy): {total_trades}")

pnl_df=df[["Close", "MA_short", "MA_long", "Position", "Signal", "Strategy_Return", "Portfolio_Value"]].copy()
pnl_df.to_csv("pnl_results.csv")

if total_strategy_return > total_market_return:
    diff=round(total_strategy_return - total_market_return, 2)
    print(f"Висновок: Стратегія виявилася ефективнішою за ринок на {diff}%!")
elif total_strategy_return < total_market_return:
    diff=round(total_market_return - total_strategy_return, 2)
    print(f"Висновок: Стратегія поступилася ринку на {diff}%. Пасивне утримання було б вигіднішим.")
else:
    print("Висновок: Дохідність стратегії та ринку виявилася однаковою.")