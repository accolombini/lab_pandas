# Neste laboratorio vamos trabalhar com Boxplot =>> queremos neste pratica trabalhar com o conceito de boxplot e suas aplicacoes praticas >>= observar outliers e a distribuicao de variaveis


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


base = pd.read_csv('D:\\teste\\FIN_DATA\\trees.csv')
# Vamos so fazer uma inspecao visual no arquivo
print(base.head())
print(base.shape)
print(type(base))
print(base.describe())
# Vamos agora trabalhar na construcao de uma figura que comporte muitos graficos => queremos em outras palavras colocar um conjunto de graficos numa mesma figura
plt.boxplot(base.Volume)
plt.show()
# Vamos agora adicionar alguns parametros ||> acompanhe <$> Vertical (vert=False) -> vamos retirar os Outliers (showfliers=False) -> Destacar a mediana (notch=True) -> Adicionando cores (patch_artistic=True)
plt.boxplot(base.Volume, vert=False, showfliers=False, notch=True, patch_artist=True)
# Vamos configurar textos tambem ||> observe
plt.title('Arvores')
plt.xlabel('Volume')
plt.show()
# Vamos agora visualizar o boxplot para todas as variaveis de nosso DataFrame ||> observe que desta forma nao e interessante
plt.boxplot(base)
plt.show()
# Vamos agora gerar um boxplot para cada variavel de interesse de nosso DataFrame
plt.boxplot(base.Volume)
plt.show()
plt.boxplot(base.Height)
plt.show()
plt.boxplot(base.Girth)
plt.show()
# Agora vamos inserir todos os boxplot numa mesma figura
plt.figure(1)
plt.subplot(2, 2, 1)
plt.boxplot(base.Volume)
plt.subplot(2, 2, 2)
plt.boxplot(base.Height)
plt.subplot(2, 2, 3)
plt.boxplot(base.Girth)
plt.subplot(2, 2, 4)
plt.boxplot(base.Volume, vert=False, showfliers=False, notch=True, patch_artist=True)
plt.title('Arvores')
plt.xlabel('Volume')
plt.show()
