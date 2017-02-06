# Teste de Lógica

Utilizei pandas e seus DataFrames, para a criação da estrutura, e posterior exportação para um 
banco SQLite3.

Primeiro, criei uma lista vazia com 100 itens. Esta lista servirá de base para cada linha do 
Dataframe, onde serão apenas posicionados os dois "X". Os "X" devem estar sempre à mesma distância 
das extremidades. Essa distância é igual ao contador do for loop, que seria igual ao número da 
linha - 1 (no caso do for loop, essa subtração não é necessária, pois o range inicia em zero)

Cada uma das linhas, já com os "X" é então transformada em um DataFrame e inserido em uma lista.
O pandas possui uma função que concatena DataFrames com estruturas iguais em um único DataFrame.
Este único DataFrame é então inserido em um banco SQLite3.