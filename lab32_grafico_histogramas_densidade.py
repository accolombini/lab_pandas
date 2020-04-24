# Neste laboratorio vamos trabalhar histograma e densidade utilizando a biblioteca seaborn


import pandas as pd 
import seaborn as srn
import matplotlib.pyplot as plt


base = pd.read_csv('D:\\teste\\FIN_DATA\\trees.csv')
# Vamos so fazer uma inspecao visual no arquivo
print(base.head())
print(base.shape)
print(type(base))
print(base.describe())

# Gerando histograma com seaborn ||> observe que ser'gerado histograma e densidade de uma unica vez
srn.distplot(base.Volume, bins=10, axlabel='Volume').set_title('Arvores')
plt.show()

# Vamos agora carregar outra base de dados =>> peso do franco x alimentacao
base2 = pd.read_csv('D:\\teste\\FIN_DATA\\chicken.csv')
# Vamos so fazer uma inspecao visual no arquivo
print(base2.head())
print(base2.shape)
print(type(base2))
print(base2.describe())
# Primeiro vamos agrupar as variaveis categoricas </> sumarizando
agrupado = base2.groupby(['feed'])['weight'].sum()
print('\nResumo do arquivo chicken.csv')
print(agrupado)
# Agora vamos gerar um histograma e densidade para cada uma das variaveis categoricas => vamos precisar de sub base de dados
teste = base2.loc[base2['feed'] == 'horsebean']
plt.figure()
plt.subplot(3, 2, 1)
srn.distplot(base2.loc[base2['feed'] == 'horsebean'].weight).set_title('horsebean')
plt.subplot(3, 2, 2)
srn.distplot(base2.loc[base2['feed'] == 'casein'].weight).set_title('casein')
plt.subplot(3, 2, 3)
srn.distplot(base2.loc[base2['feed'] == 'linseed'].weight).set_title('linseed')
plt.subplot(3, 2, 4)
srn.distplot(base2.loc[base2['feed'] == 'meatmeal'].weight).set_title('meatmeal')
plt.subplot(3, 2, 5)
srn.distplot(base2.loc[base2['feed'] == 'soybean'].weight).set_title('soybean')
plt.subplot(3, 2, 6)
srn.distplot(base2.loc[base2['feed'] == 'sunflower'].weight).set_title('sunflower')
# Observe a instrucao a seguir =>> ela foi inserida para evitar superposicao dos graficos |||> teste com e sem ela e observe as mudancas
plt.tight_layout()
plt.show()

# Caso nao queira por exemplo o histograma =>> observe como faze-lo
plt.figure()
plt.subplot(3, 2, 1)
srn.distplot(base2.loc[base2['feed'] == 'horsebean'].weight, hist=False).set_title('horsebean')
plt.subplot(3, 2, 2)
srn.distplot(base2.loc[base2['feed'] == 'casein'].weight, hist=False).set_title('casein')
plt.subplot(3, 2, 3)
srn.distplot(base2.loc[base2['feed'] == 'linseed'].weight, hist=False).set_title('linseed')
plt.subplot(3, 2, 4)
srn.distplot(base2.loc[base2['feed'] == 'meatmeal'].weight, hist=False).set_title('meatmeal')
plt.subplot(3, 2, 5)
srn.distplot(base2.loc[base2['feed'] == 'soybean'].weight, hist=False).set_title('soybean')
plt.subplot(3, 2, 6)
srn.distplot(base2.loc[base2['feed'] == 'sunflower'].weight, hist=False).set_title('sunflower')
# Observe a instrucao a seguir =>> ela foi inserida para evitar superposicao dos graficos |||> teste com e sem ela e observe as mudancas
plt.tight_layout()
plt.show()
# Como foi suprimido o histograma poderia ter sido feito para o diagrama de dispersao
