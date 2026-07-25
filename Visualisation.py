import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("pnl_results.csv", index_col=0, parse_dates=True)


# наші пареметри
short_window = 20
long_window = 100
start_capital = 10000.0


plt.figure(figsize=(14, 10))
plt.style.use('seaborn-v0_8-darkgrid')

plt.figure(figsize=(14, 10))
plt.style.use('seaborn-v0_8-darkgrid')

ax1 = plt.subplot(2, 1, 1)
plt.title('Торгова стратегія: Перетин ковзних середніх (BRK-B)', fontsize=16, fontweight='bold')
plt.plot(df.index, df['Close'], label='Ціна закриття (Close)', color='black', alpha=0.6, linewidth=1.5)
plt.plot(df.index, df['MA_short'], label=f'MA Short ({short_window})', color='blue', linestyle='--', alpha=0.8)
plt.plot(df.index, df['MA_long'], label=f'MA Long ({long_window})', color='orange', linestyle='--', alpha=0.8)

buy_signals = df[df['Signal'] == 'Buy']
plt.scatter(buy_signals.index, buy_signals['Close'], label='Купівля (Buy)', marker='^', color='green', s=150, zorder=5)

sell_signals = df[df['Signal'] == 'Sell']
plt.scatter(sell_signals.index, sell_signals['Close'], label='Продаж (Sell)', marker='v', color='red', s=150, zorder=5)


#збереження файлу
plt.tight_layout()
output_filename = 'strategy_visualization.png'
plt.savefig(output_filename, dpi=300)
plt.close()

print(f"Графік успішно збережено у файл: {output_filename}")