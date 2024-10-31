import pandas as pd
import numpy as np

bovespa_data = pd.read_excel("C:\\Users\\Jorge\\OneDrive\\Quantiles\\bovespa_data.xlsx", sheet_name='Sheet1')
bovespa_data['Date'] = pd.to_datetime(bovespa_data['Date'])
bovespa_data.set_index('Date', inplace=True)

initial_cash = 100000

class simulador: 

    initial_cash = 100000

    def __init__(self, portfolio, cash):
        self.portfolio = {ticker: 0 for ticker in bovespa_data.columns}
        self.cash = initial_cash

    def buy(self, ticker, date, weight):
        date = pd.to_datetime(date)
        price = bovespa_data[ticker].loc[date]
        cotas = np.floor((self.cash * weight) / price)
        self.portfolio[ticker] += cotas
        self.cash -= cotas * price

        
    def sell(self, ticker, date, weight):
        date = pd.to_datetime(date)
        price = bovespa_data[ticker].loc[date]
        cotas = np.floor((self.cash * weight) / price)
        self.portfolio[ticker] -= cotas
        self.cash += cotas * price

    def backtest(self, date):
        date = pd.to_datetime(date)
        value = 0
        for ticker, shares in self.portfolio.items():
            price = bovespa_data[ticker].loc[date]
            value += shares * price
        return value + self.cash
        




