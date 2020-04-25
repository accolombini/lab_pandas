# Neste laboratorio vamos trabalhar com graficos de dispersao utilizando a biblioteca seaborn. Queremos nesta pratica explorar variaveis categoricas e variaveis continuas <$> Acompanhe


import pandas as pd 
import seaborn as srn
import matplotlib.pyplot as plt


base = pd.read_csv('D:\\teste\\FIN_DATA\\co2.csv')
# Vamos so fazer uma inspecao visual no arquivo
print(base.head())
print(base.tail())
print(base.shape)
print(type(base))
print(base.describe())

# Primeiro vamos trabalhar com as duas variaveis continuas
srn.scatterplot(base.conc, base.uptake)
plt.show()
# Vamos agora inserir um novo parametro atraves da diretiva hue => adicionando o tipo ao grafico >>= obeserve que o hue também gera uma legenda automaticamente
srn.scatterplot(base.conc, base.uptake, hue=base.Type)
plt.show()
# Podemos agora trabalhar com condicionais e melhorar nossos resultados => precisaremos dividir nossa base de dados para atingir esse objetivo ||> suponha que queiramos separar os dados azuis dos laranjas
q = base.loc[base['Type'] == 'Quebec']
m = base.loc[base['Type'] == 'Mississippi']
# Agora vamos criar o subgrafico
plt.figure()
plt.subplot(1, 2, 1)
srn.scatterplot(q.conc, q.uptake).set_title('Quebec')
plt.subplot(1, 2, 2)
srn.scatterplot(m.conc, m.uptake).set_title('Mississippi')
# Para melhorar a visualizacao vamos usar o recurso abaixo => acompanhe
plt.tight_layout()
plt.show()

# Vamos agora a outro exemplo => refrigerado e nao refrigerado
ch = base.loc[base['Treatment'] == 'chilled']
nc = base.loc[base['Treatment'] == 'nonchilled']

plt.figure()
plt.subplot(1, 2, 1)
srn.scatterplot(q.conc, q.uptake).set_title('chilled')
plt.subplot(1, 2, 2)
srn.scatterplot(m.conc, m.uptake).set_title('nonchilled')
# Para melhorar a visualizacao vamos usar o recurso abaixo => acompanhe
plt.tight_layout()
plt.show()

# Vamos agora para praticar explorar uma segunda base de dados =>> tambem com atributos categoricos e numericos
base2 = pd.read_csv('D:\\teste\\FIN_DATA\\esoph.csv')
# Vamos so fazer uma inspecao visual no arquivo
print(base2.head())
print(base2.tail())
print(base2.shape)
print(type(base2))
print(base2.describe())
# Vamos usar agora um novo metodo da biblioteca seaborn chamada .catplot()
srn.catplot(x='alcgp', y='ncontrols', data=base2)
plt.show()
# Para melhorar um pouco a visualizacao vamos usar o parametro jitter => afasta os pontos mas nao altera os dados, no caso vamos usar jitter = False observe o efeito
srn.catplot(x='alcgp', y='ncontrols', data=base2, jitter=False)
plt.show()
# Agora vamos introduzir mais uma coluna para realizar o agrupamento => muito interessante para realizar o comparativo entre as variaveis categoricas e continuas
srn.catplot(x='alcgp', y='ncontrols', data=base2, col='tobgp')
plt.show()
