import pandas as pd
import numpy as np

df = pd.read_csv("brk_-_b_data.csv", index_col=0, parse_dates=True)
short_window = 20
long_window = 100

#Розрахунок ковзних за допомогою .rolling().mean()

df["MA_short"] = df["Close"].rolling(window=short_window).mean()
df["MA_long"] = df["Close"].rolling(window=long_window).mean()



# # Оптимізую стратегію за допомогою буферу, адже результат є критично не задовільнім

df["Position"] = np.nan # робимо це для сімейного достатку у операції ffill().fillna(0)
buffer = df["MA_long"] * 0.05
#все було зроблено для цього буферу
df.loc[df["MA_short"] > df["MA_long"] , "Position"] = 1
df.loc[df["MA_short"] < (df["MA_long"] - buffer), "Position"] = 0

df["Position"] = df["Position"].ffill().fillna(0)
# df["Position"] = 0
# старий концепт
# df.loc[df["MA_short"] > df["MA_long"], "Position"] = 1
#
df["ssignal_change"] = df["Position"].diff()

#Вводимо сигнали, аби зараз усі були на Hold
df["Signal"] = "Hold"
#Ввів умови того, якими стають бути сигнали відповідно того як змінюється перетин ковзних
df.loc[df["ssignal_change"] == 1, "Signal"] = "Buy"
df.loc[df["ssignal_change"] == -1, "Signal"] = "Sell"

df = df.dropna(subset=["MA_long"]).copy()


print(f"Кількість сигналів Buy: {(df['Signal']=='Buy').sum()}")
print(f"Кількість сигналів Sell: {(df['Signal']=='Sell').sum()}")

signals_df = df[["Close", "MA_short", "MA_long", "Position", "Signal"]].copy()

signals_df = signals_df.round(2)
signals_df.to_csv("trading_signals.csv")

df = df.round(2)