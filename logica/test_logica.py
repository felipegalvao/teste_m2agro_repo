'''
Aqui, usarei Dataframes do Pandas para criar a estrutura do Teste de Lógica. Usarei um for loop
para criar cada linha, onde os X de cada linha devem estar distante das extremidades no mesmo 
valor do contador do loop. No fim, exportarei o Dataframe para um BD Sqlite3
'''

import pandas as pd
import sqlite3

num_linhas_colunas = 100

list_of_dataframes = []
base_list = []

# Criar uma lista base, com 100 itens vazios
for i in range(num_linhas_colunas):
    base_list.append('')

# Coloca os 'X' nos itens de acordo com o contador
for i in range(num_linhas_colunas):
    new_list = list(base_list)
    new_list[i] = 'X'
    new_list[len(new_list)-1-i] = 'X'
    list_of_dataframes.append(pd.DataFrame([new_list]))

# Concatena os Dataframes, criando um único dataframe com a estutura desejada (um grande X)
df = pd.concat(list_of_dataframes)

# Conecta ao banco Sqlite3 e salva o dataframe na tabela m2agro
conn = sqlite3.connect('m2agro.sqlite3')
df.to_sql('m2agro', conn)