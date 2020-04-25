# Neste laboratorio vamos trabalhar com graficos 3D


import pandas as pd 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


base = pd.read_csv('D:\\teste\\FIN_DATA\\orchard.csv')
# Vamos so fazer uma inspecao visual no arquivo
print(base.head())
print(base.shape)
print(type(base))
print(base.describe())
# O objetivo desta pratica e a geracao de um grafico 3D a partir das tres variaveis do nosso conjunto de dados
figura = plt.figure()
# Vamos criar uma variavel eixo para receber os atributos da figura, observe oparametro subplot(1, 1, 1) normalmente utilizado para representar mais de uma figura, aqui sera usado para uma unica figura 3D
eixo = figura.add_subplot(1, 1, 1, projection='3d')
eixo.scatter(base.decrease, base.rowpos, base.colpos)
eixo.set_xlabel('decrease')
eixo.set_ylabel('rowpos')
eixo.set_zlabel('colpos')
plt.show()
