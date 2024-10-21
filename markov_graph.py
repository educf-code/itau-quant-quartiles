import matplotlib.pyplot as plt
import pandas as pd

# file_path = "C:\\Users\\Jorge\\OneDrive\\Quantiles\\bovespa_data.xlsx"
sheet_name = 'Sheet1'

df = pd.read_excel(file_path, sheet_name=sheet_name, header=0)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
# print(df.columns)

stock_values = df['WEGE3.SA']
percentage_growth = stock_values.pct_change() * 100

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(stock_values.index, stock_values, label='WEGE3.SA', color='black')

for i in range(len(stock_values) - 1):
    color = 'green' if percentage_growth.iloc[i+1] >= 0 else 'yellow'
    ax.axvspan(stock_values.index[i], stock_values.index[i + 1], color=color, alpha=0.8)

ax.set_xlabel('Data')
ax.set_ylabel('Valor da Ação')
ax.set_title('Valor da Ação com cores indicando o regime de crescimento do preço')
ax.legend()
plt.show()