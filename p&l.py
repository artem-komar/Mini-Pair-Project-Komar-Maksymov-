import pandas as pd

df = pd.read_csv("trading_signals.csv", index_col=0, parse_dates=True)

start_capital= 10000.0
shares_count= 13

df["Market_Return"]= df["Close"].pct_change()
market_growth_factor= 1 + df["Market_Return"]
df["Cum_Market_Return"]= market_growth_factor.cumprod() - 1
total_market_return= df["Cum_Market_Return"].iloc[-1] * 100

df["Price_Change"]= df["Close"].diff()
df["Daily_PnL"]= df["Price_Change"]*df["Position"].shift(1) * shares_count
df["Daily_PnL"]= df["Daily_PnL"].fillna(0)
df["Cum_PnL"]= df["Daily_PnL"].cumsum()

df["Portfolio_Value"]= (start_capital + df["Cum_PnL"]).round(2)
df["Strategy_Return"]= df["Daily_PnL"]/start_capital

final_balance= df["Portfolio_Value"].iloc[-1]
net_profit= round(final_balance -start_capital, 2)
total_strategy_return=(net_profit/start_capital) *100
total_trades= sum(df["Signal"]=="Buy")
print(f"Початковий депозит:${round(start_capital, 2)}")
print(f"Обрана кількість акцій у позиції: {shares_count} шт.")
print(f"Кінцевий баланс:${round(final_balance, 2)}")
print(f"Абсолютний прибуток/збиток:${round(net_profit, 2)}")
print(f"Дохідність стратегії: {round(total_strategy_return, 2)}%")
print(f"Дохідність ринку (Buy & Hold):{round(total_market_return, 2)}%")
print(f"Кількість угод (Buy):{total_trades}")

pnl_df= df[["Close", "MA_short", "MA_long", "Position", "Signal", "Strategy_Return", "Portfolio_Value"]].copy()
pnl_df.to_csv("pnl_results.csv")

if total_strategy_return > total_market_return:
    diff= round(total_strategy_return - total_market_return, 2)
    print(f"Висновок: Стратегія виявилася ефективнішою за ринок на {diff}%!")
elif total_strategy_return < total_market_return:
    diff= round(total_market_return - total_strategy_return, 2)
    print(f"Висновок: Стратегія поступилася ринку на {diff}%. Пасивне утримання було б вигіднішим.")
else:
    print("Висновок: Дохідність стратегії та ринку виявилася однаковою.")