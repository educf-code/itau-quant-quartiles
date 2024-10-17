import pandas as pd

file_path = "C:\\Users\\Jorge\\OneDrive\\Quantiles\\bovespa_data.xlsx"
sheet_name = 'Percentuais'

df = pd.read_excel(file_path, sheet_name=sheet_name, header=0)

tickers = df.columns.tolist()

transition_matrices = {ticker: [[]] for ticker in tickers}
transition_matrices.pop('Date', None)

# for ticker in transition_matrices:
    # TODO: Considerar dez estados possíveis:
    # Ação cai 4%+
    # Ação cai 3-4%
    # Ação cai 2-3%
    # Ação cai 1-2%
    # Ação cai 0-1%
    # Ação sobe 0-1%
    # Ação sobe 1-2%
    # Ação sobe 2-3%
    # Ação sobe 3-4%
    # Ação sobe 4%+
    # Para cada ação, se em um dado dia temos um estado X e no seguinte temos Y, adicionar 1 ao count do número da transições X -> Y
    # Por exemplo, se no dia 52 a ação está no estado 3 e no dia 53 está no estado 4, setar count[2][3] += 1
    # Ao final, dividir cada count pelo total de transições (total de elementos na coluna - 1) para obter a matriz de transição


print(transition_matrices)