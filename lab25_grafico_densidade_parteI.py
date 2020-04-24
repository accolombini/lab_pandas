# Neste laboratorio vamos trabalhar mais de perto com diagramas de dispersao


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns


base = pd.read_csv('D:\\teste\\FIN_DATA\\trees.csv')
# Vamos so fazer uma inspecao visual no arquivo
print(base.head())
print(base.shape)
print(type(base))
print(base.describe())
# Feito isso temos uma visao geral => vamos agora aos graficos
plt.hist(base.iloc[:,1], bins=10)
plt.show()
# Vamos agora usar a biblioteca seaborn => obsersve
sns.distplot(base.iloc[:,1])
plt.show()
# Agora vamos ver algumas opcoes para melhorar a aparencia do nosso grafico => atento ao uso do diconario para definir a cor de envoltoria <$> hist -> histograma kde -> densidade
sns.distplot(base.iloc[:,1], hist=True, kde=True, bins = 6, color='blue', hist_kws={'edgecolor' : 'black'})
plt.show()
