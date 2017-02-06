import pandas as pd

num_linhas_colunas = 10

list_of_dataframes = []
base_list = []

for i in range(num_linhas_colunas):
    base_list.append('')

for i in range(10):
    new_list = list(base_list)
    new_list[i] = 'X'
    new_list[len(new_list)-1-i] = 'X'
    list_of_dataframes.append(pd.DataFrame([new_list]))

df = pd.concat(list_of_dataframes)
df.to_csv('data.csv', index=False)