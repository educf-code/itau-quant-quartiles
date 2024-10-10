import yfinance as yf
import pandas as pd
import os

# Tickers da B3
b3_tickers = [
    "ABEV3.SA", "AZUL4.SA", "B3SA3.SA", "BBAS3.SA", "BBDC3.SA", "BBDC4.SA",
    "BBSE3.SA", "BEEF3.SA", "BPAC11.SA", "BRAP4.SA", "BRFS3.SA", "BRKM5.SA",
    "BRML3.SA", "BTOW3.SA", "CCRO3.SA", "CIEL3.SA", "CMIG4.SA", "CSAN3.SA",
    "CSNA3.SA", "CVCB3.SA", "CYRE3.SA", "ECOR3.SA", "EGIE3.SA", "ELET3.SA",
    "ELET6.SA", "EMBR3.SA", "ENBR3.SA", "ENGI11.SA", "EQTL3.SA", "EZTC3.SA",
    "FLRY3.SA", "GGBR4.SA", "GOAU4.SA", "GOLL4.SA", "HAPV3.SA", "HGTX3.SA",
    "HYPE3.SA", "IGTA3.SA", "IRBR3.SA", "ITSA4.SA", "ITUB4.SA", "JBSS3.SA",
    "KLBN11.SA", "LAME4.SA", "LREN3.SA", "MGLU3.SA", "MRFG3.SA", "MRVE3.SA",
    "MULT3.SA", "NTCO3.SA", "PCAR3.SA", "PETR3.SA", "PETR4.SA", "PRIO3.SA",
    "QUAL3.SA", "RADL3.SA", "RAIL3.SA", "RENT3.SA", "SANB11.SA", "SBSP3.SA",
    "SULA11.SA", "SUZB3.SA", "TAEE11.SA", "TIMP3.SA", "TOTS3.SA", "UGPA3.SA",
    "USIM5.SA", "VALE3.SA", "VIVT3.SA", "VVAR3.SA", "WEGE3.SA", "YDUQ3.SA"
]

def download(tickers):
    data = {}
    for ticker in tickers:
        try:
            data[ticker] = yf.download(ticker)['Close']
            print(f"Baixando dados de {ticker}")
        except Exception as e:
            print(f"Erro ao baixar dados de {ticker}: {e}")
    return data

dados = download(b3_tickers)
df = pd.DataFrame(dados)
df.to_excel('dados_b3.xlsx', index=True)
print("Dados salvos")

# dados = download(b3_tickers)
# df = pd.DataFrame(dados)
# output_path = os.path.join(os.path.expanduser(""), "dados_b3.xlsx")
# df.to_excel(output_path, index=True)
# print(f"Dados salvos em '{output_path}'")