# Neste laboratorio vamos trabalhar mais de perto com histogramas


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


base = pd.read_csv('D:\\teste\\FIN_DATA\\trees.csv')
print(base.head())
# Preparando para o grafico ==> observe o uso do np. no iloc estamos definindo que queremos todas as linhas e a coluna 1 (Height)
h = np.histogram(base.iloc[:,1], bins='auto')
# Observe o que esta na variavel h (importante) => analise
print(h)
plt.hist(base.iloc[:,1])
plt.show()
# Alterando bins => observe
plt.hist(base.iloc[:,1], bins=6)
plt.show()
# Vamos agora fazer algumas configurações no nosso grafico
plt.hist(base.iloc[:,1], bins=6)
plt.title('Arvores')
plt.ylabel('Frequencia')
plt.xlabel('Altura')
plt.show()
