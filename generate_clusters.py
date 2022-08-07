import pandas as pd
import random

centros = [[0, 0, 0, 0], [6, 0, 0, 2.5], [2.1, 1.6, 1.5, 0]]
columns = [0, 1, 2, 3]
data = []
    
for row in range(250):
    data.append([])
    data[row] = [x + random.gauss(x, 1.5) for x in centros[random.randint(0, 2)]]

pd.DataFrame(data).to_csv('./data/example_data1.csv')