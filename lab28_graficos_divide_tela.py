# Neste laboratorio vamos trabalhar divisao de tela =>> queremos neste pratica trabalhar com o conceito de subgraficos


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
plt.figure(1)
# Vamos agora criar o primeiro grafico que e o girth com volume => paramentors de subplot(x1 -> numero de linhas, x2 -> numero de colunas x3 -> id do grafico =>> queremos neste caso quatro graficos em uma mesma figura >>= no caso dentro da figura(1)
# Grafico 1 => Girth x Volume
plt.subplot(2, 2, 1)
plt.scatter(base.Girth, base.Volume)
# Grafico 2 => Girth x Height
plt.subplot(2, 2, 2)
plt.scatter(base.Girth, base.Height)
# Grafico 3 => Height x Volume
plt.subplot(2, 2, 3)
plt.scatter(base.Height, base.Volume)
# Grafico 4 => Histograma com Volume
plt.subplot(2, 2, 4)
plt.hist(base.Volume)
plt.show()
# Observe que todos os 4 subgraficos pertecem a figura 1 definida acima
