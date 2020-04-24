# Neste laboratorio vamos trabalhar boxplot utilizando a biblioteca seaborn


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as srn


base = pd.read_csv('D:\\teste\\FIN_DATA\\trees.csv')
# Vamos so fazer uma inspecao visual no arquivo
print(base.head())
print(base.shape)
print(type(base))
print(base.describe())
# Gerando boxplot com a biblioteca seaborn
srn.boxplot(base.Volume).set_title('Arvores')
plt.show()
# Observe que conseguiresmos com uma linha de codigo trabalhar todas as variaveis em um unico grafico >>= acompnhe
srn.boxplot(data=base).set_title('Arvores')
plt.show()
