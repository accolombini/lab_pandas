# Neste laboratorio vamos trabalhar mais de perto com diagramas de dispersao com legendas =>> queremos neste grafico explorar melhro as variaveis categoricas, o objetivo e mostrar a associacao dos dados numericos com as variaveis categoricas


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


base = pd.read_csv('D:\\teste\\FIN_DATA\\co2.csv')
# Vamos so fazer uma inspecao visual no arquivo
print(base.head())
print(base.shape)
print(type(base))
print(base.describe())
# Vamos organizar as variaveis de interesse
x = base.conc
y = base.uptake
# Vamos buscar os nomes das categorias
unicos = list(set(base.Treatment))
print('\nVamos inspecionar nossa variavel unicos =>> observe que sao duas categorias')
print(unicos)
# Queremos agora associar os valores das variaveis x e y as categorias de nossa lista unicos
for i in range(len(unicos)):
    indice = base.Treatment == unicos[i]
    plt.scatter(x[indice], y[indice], label=unicos[i])
plt.legend(loc='lower right')
plt.show()
