import pandas as pd

#######################
# file_path = r""
data = pd.read_excel(file_path)

percentual_data = pd.DataFrame()
percentual_data['Date'] = data.iloc[:, 0]

for column in data.columns[1:]:
    percentual_data[column] = 100 * (data[column] - data[column].shift(1)) / data[column].shift(1)

#percentual_data = percentual_data.dropna()

with pd.ExcelWriter(file_path, engine='openpyxl', mode='a') as writer:
    percentual_data.to_excel(writer, sheet_name='Percentuais', index=False)