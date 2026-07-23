import pandas as pd
import yfinance as yf


start_date="2024-01-01"
end_date="2026-07-22"
ticker_name="BRK-B"
exchange="NYSE (New York Stock Exchange)"
currency="USD"

print(f"Обраний актив: {ticker_name}")
print(f"Біржа: {exchange}")
print(f"Валюта: {currency}")
print(f"Отримані дані з {start_date} по {end_date} включно.")
raw_data=yf.download(ticker_name, start=start_date, end=end_date)

df=raw_data[["Open", "High", "Low", "Close", "Volume"]].copy()
df=df.dropna()

print(f"Дані очищено.")
print(f"Кількість торгових днів: {len(df)}")
print(f"Перші 5 позицій")
print(df.head())
print(f"Останні 5 позицій")
print(df.tail())
print(f"Загальна статистика:")
print(df.describe())