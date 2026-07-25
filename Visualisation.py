import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("pnl_results.csv", index_col=0, parse_dates=True)

plt.figure(figsize=(14, 10))
plt.style.use('seaborn-v0_8-darkgrid')

plt.tight_layout()
output_filename = 'strategy_visualization.png'
plt.savefig(output_filename, dpi=300)
plt.close()

print(f"Графік успішно збережено у файл: {output_filename}")