import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("p&l.py", index_col=0, parse_dates=True)

plt.figure(figsize=(14, 10))
plt.style.use('seaborn-v0_8-darkgrid')