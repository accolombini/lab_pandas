# Neste laboratorio vamos trabalhar mais de perto com diagramas de dispersao =>> queremos neste grafico avaliarmos se existe uma relacao entre variaveis continuas


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
# Feito isso temos uma visao geral => vamos agora aos graficos => faremos isso usando o plano cartesiano ||> observe
plt.scatter(base.Girth, base.Volume)
plt.title('Arvores')
plt.xlabel('Volume')
plt.ylabel('Circunferencia')
plt.show()
# Vamos agora personalizar um pouco nosso grafico ||> observe -> facecolors = none => estamos tirando o preencimento
plt.scatter(base.Girth, base.Volume, color='cyan', facecolors='none', marker='^')
plt.title('Arvores')
plt.xlabel('Volume')
plt.ylabel('Circunferencia')
plt.show()
# Vamos agora visualizar os mesmos dados utilizando o grafico de linhas ||> acompanhe
plt.plot(base.Girth, base.Volume)
plt.show()
# Como foi possivel perceber, temos um problema de superposicao =>> agora vamos tratar esse evento utilizando a biblioteca seaborn e encontrar a melhor curva de linearidade entre nossas variaveis (linha de regressao)
sns.regplot(base.Girth, base.Volume, data=base)
plt.show()
# Neste proximo grafico iremos adiconar um pouco de ruido no eixo x (x_jitter) e retirar a curva de regressao (fit_reg = false) ||> a ideia de usar o jitter e para espacar os pontos superpostos para uma melhor visualizacao <$> cabe a voce os ajustes -> vou usar 0.3 (experimente outros valores)
sns.regplot(base.Girth, base.Volume, data=base, x_jitter=0.3, fit_reg=False)
plt.show()
# Neste proximo grafico iremos adiconar um pouco de ruido no eixo y (y_jitter) e retirar a curva de regressao (fit_reg = false) ||> a ideia de usar o jitter e para espacar os pontos superpostos para uma melhor visualizacao <$> cabe a voce os ajustes -> vou usar 0.2 (experimente outros valores)
sns.regplot(base.Girth, base.Volume, data=base, y_jitter=0.2, fit_reg=False)
plt.show()
# Importante =>> o parametro jitter nao altera dados apenas a visualizacao ok
