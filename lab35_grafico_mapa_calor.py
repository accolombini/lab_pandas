# Neste laboratorio vamos explorar o mapa de calor => acompnhe podera ser muito utili


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


base = pd.read_csv('D:\\Users\Angelo\AULAS\\titanic_train.csv')
# Vamos so fazer uma inspecao visual no arquivo
print(base.head())
print(base.tail())
print(base.shape)
print(type(base))
print(base.describe())

# Precisamos da correlacao para nossos trabalhos, inicialmente todas as variaveis estao dispostas em colunas => precisamos tambem de linhas >>= acompanhe
cor = base.corr()
print('\nAnalisando novamente nossos dados => observe as mudancas')
print(cor.head())
print(cor.shape)
# Construindo o mapa de calor =>> observe
plt.rcParams['figure.figsize'] = [10,8]
sns.heatmap(cor, annot=True)
plt.show()
