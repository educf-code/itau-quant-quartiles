import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

file_path = "C:\\Users\\Jorge\\OneDrive\\Quantiles\\bovespa_data.xlsx"
sheet_name = 'Percentuais'

df = pd.read_excel(file_path, sheet_name=sheet_name, header=0)

tickers = df.columns.tolist()

transition_matrices = {ticker: [[]] for ticker in tickers}
transition_matrices.pop('Date', None)

for ticker in transition_matrices:
    counts = [[0] * 10 for _ in range(10)]
    total_transitions = len(df[ticker]) - 1

    for i in range(total_transitions):
        current_state = df[ticker].iloc[i]
        next_state = df[ticker].iloc[i + 1]

        if current_state <= -4:
            current_index = 0
        elif -4 < current_state <= -3:
            current_index = 1
        elif -3 < current_state <= -2:
            current_index = 2
        elif -2 < current_state <= -1:
            current_index = 3
        elif -1 < current_state <= 0:
            current_index = 4
        elif 0 < current_state <= 1:
            current_index = 5
        elif 1 < current_state <= 2:
            current_index = 6
        elif 2 < current_state <= 3:
            current_index = 7
        elif 3 < current_state <= 4:
            current_index = 8
        else:
            current_index = 9

        if next_state <= -4:
            next_index = 0
        elif -4 < next_state <= -3:
            next_index = 1
        elif -3 < next_state <= -2:
            next_index = 2
        elif -2 < next_state <= -1:
            next_index = 3
        elif -1 < next_state <= 0:
            next_index = 4
        elif 0 < next_state <= 1:
            next_index = 5
        elif 1 < next_state <= 2:
            next_index = 6
        elif 2 < next_state <= 3:
            next_index = 7
        elif 3 < next_state <= 4:
            next_index = 8
        else:
            next_index = 9

        counts[current_index][next_index] += 1

    transition_matrix = [[count / total_transitions for count in row] for row in counts]
    transition_matrices[ticker] = transition_matrix

# print(transition_matrices) 

def transition_matrix(ticker):
    counts = [[0] * 10 for _ in range(10)]
    total_transitions = len(df[ticker]) - 1

    for i in range(total_transitions):
        current_state = df[ticker].iloc[i]
        next_state = df[ticker].iloc[i + 1]

        if current_state <= -4:
            current_index = 0
        elif -4 < current_state <= -3:
            current_index = 1
        elif -3 < current_state <= -2:
            current_index = 2
        elif -2 < current_state <= -1:
            current_index = 3
        elif -1 < current_state <= 0:
            current_index = 4
        elif 0 < current_state <= 1:
            current_index = 5
        elif 1 < current_state <= 2:
            current_index = 6
        elif 2 < current_state <= 3:
            current_index = 7
        elif 3 < current_state <= 4:
            current_index = 8
        else:
            current_index = 9

        if next_state <= -4:
            next_index = 0
        elif -4 < next_state <= -3:
            next_index = 1
        elif -3 < next_state <= -2:
            next_index = 2
        elif -2 < next_state <= -1:
            next_index = 3
        elif -1 < next_state <= 0:
            next_index = 4
        elif 0 < next_state <= 1:
            next_index = 5
        elif 1 < next_state <= 2:
            next_index = 6
        elif 2 < next_state <= 3:
            next_index = 7
        elif 3 < next_state <= 4:
            next_index = 8
        else:
            next_index = 9

        counts[current_index][next_index] += 1

    transition_matrix = [[count / total_transitions for count in row] for row in counts]
    return pd.DataFrame(transition_matrix)

exemplo_WEGE = transition_matrices['WEGE3.SA']
df_WEGE = pd.DataFrame(exemplo_WEGE)
print(df_WEGE)


sum = 0
for i in range(10):
    for j in range(10):
        sum += exemplo_WEGE[i][j]
print(sum)


def markov_graph(matrix):
    G = nx.DiGraph()

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > 0:
                G.add_edge(i, j, weight=matrix[i][j])

    pos = nx.spring_layout(G)
    edge_labels = {(i, j): f'{matrix[i][j]:.4f}' for i, j in G.edges()}

    nx.draw(G, pos, with_labels=True, node_size=700, node_color='green', font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black')

    plt.show()

markov_graph(exemplo_WEGE)
