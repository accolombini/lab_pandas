# Neste laboratorio vamos trabalhar com graficos de Barras e graficos de setores =>> queremos neste pratica trabalhar com o conceito de variaveis categoricas, onde desejamos sumarizar valores. Observe que o matplotlib sera usado apenas para exibir os graficos na tela


import pandas as pd 
import matplotlib.pyplot as plt 


base = pd.read_csv('D:\\teste\\FIN_DATA\\insect.csv')
# Vamos so fazer uma inspecao visual no arquivo
print(base.head())
print(base.shape)
print(type(base))
print(base.describe())
# Agora vamos agrupar as variaveis categoricas >>= spray -> as variaveis categoricas a sere agrupadas -> count coluna com os valores que queremos somar atribuindo a cada variavel categorica (sumarizando)
agrupado = base.groupby(['spray'])['count'].sum()
print('\nResumo das variaveis categoricas')
print(agrupado)
# Feito o agrupamento vamos agora gerar os graficos de barras =>> observe que estamos usando a biblioteca pandas diretamente
agrupado.plot.bar(color='cyan')
plt.show()
# Feito o agrupamento vamos agora gerar os graficos de pizza=>> observe que estamos usando a biblioteca pandas diretamente
agrupado.plot.pie(legend=True)
plt.show()
