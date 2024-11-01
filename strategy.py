from backtest_markov import simulador
from transition_matrix import transition_matrix
import pandas as pd

def input_vector():
    numbers = []
    for i in range(10):
        num = float(input(f"Entre o numero {i}: "))
        numbers.append(num)
    
    if sum(numbers) != 1:
        raise ValueError("Numeros devem ter soma 1")
    
    return numbers



def best_scenario(ticker):
    initial = input_vector()
    probabilities = {}
    matrix = transition_matrix(ticker)
    for a in range(10):
        for b in range(10):
            for c in range(10):
                        probabilities[(a,b,c)] = initial[a] * matrix.iloc[a,b] * matrix.iloc[b,c]

    max_key = max(probabilities, key=probabilities.get)
    print(f"Max key: {max_key}, Max value: {probabilities[max_key]}")

best_scenario('ITUB4.SA')
