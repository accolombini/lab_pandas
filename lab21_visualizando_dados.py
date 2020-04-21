# Nesta pratica nosso objetivo e manipular graficamente os dados promovendo formas alternativas de visualizacao e analise => lembrando que podemos estar falando de arquivos gigantescos
# Em se tratando de Big Data e IoT temos os 4 Vs >>= V => Volume V => Velocidade V => Variedade V => Veracidade
# Os principais tipos de arquivos que iremos trabalhar sao: .txt, .csv e .xlx
# Arquivos .txt => normalmente empregados para informacoes nao estruturadas
# Arquivos .csv => sao os mais comuns encontrados por ai
# Arquivos .xlsx => sao arquivos do Excel
# Resumo [Dado] =>> [Estrutura] =>> [Arquivar ~> Salvar]


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


# Uma dica que pode ser util e visualizar os estilos de graficos a sua pronta disposicao, basta usar a diretiva a seguir => plt.style.available
print(plt.style.available)
# A seguir definimos que queremos que nossa figura seja plotada num retangulo (rcParams) de dimensoes (11, 7)+> as dimensoes seguem o padrao (x, y)
plt.rcParams['figure.figsize'] = (11, 7)
# Vamos carregar os dados que serao analisados =>> no caso os dados do Titanic que estao no formato .csv
d = pd.read_csv('D:\\Users\Angelo\AULAS\\titanic_train.csv')
# Fazendo uma rapida inspecao nos dados temos
print('\nInspecao inicial nos dados')
print(d.head(3))
print('\nA dimensao do arquivo de treino')
print(d.shape)
print('\nUma primeira inspecao atraves da estatistica descritiva')
print(d.describe())
# Para o primeiro grafico de dispesao para visualizar a relacao passageiros por idade dos passageiros do Titanic
plt.scatter(d.PassengerId, d.Age, edgecolors='r', plotnonfinite=True, linewidths=2)
plt.title('Informacoes dos Passageiros do Titanic')
plt.xlabel('Passageiro')
plt.ylabel('Idade')
plt.show()
# Vamos agora expandir a area de plotagem e aumentar as legendas
plt.rcParams['figure.figsize'] = (15, 7)
plt.scatter(d.PassengerId, d.Age, edgecolors='r', plotnonfinite=True, linewidths=2)
plt.title('Informacoes dos Passageiros do Titanic', size=18)
plt.xlabel('Passageiro', size=16)
plt.ylabel('Idade', size=16)
plt.show()

# Agora vamos usar a propria biblioteca pandas para gerar nossos graficos
d.Age.plot()
plt.title('Informacoes dos Passageiros do Titanic', size=18)
plt.xlabel('Passageiro', size=16)
plt.ylabel('Idade', size=16)
plt.show()

# Vamos agora usando a biblioteca pandas gerar o grafico de todas as colunas numericas de nosso DataFrame
d.plot()
plt.title('Informacoes dos Passageiros do Titanic', size=18)
plt.show()

# Podemos tambem usar uma forma a seguinte sintaxe do matplotlib

plt.plot(d.Age, '*')
plt.title('Informacoes dos Passageiros do Titanic', size=18)
plt.xlabel('Passageiro', size=16)
plt.ylabel('Idade', size=16)
plt.show()

# Vamos usar o scatter para visualizar a idade dos passageiros adicionando cores e marcadores
plt.scatter(d.PassengerId, d.Age, color='green', edgecolors='r', marker='>', plotnonfinite=True, linewidths=2)
plt.title('Informacoes dos Passageiros do Titanic', size=18)
plt.xlabel('Passageiro', size=16)
plt.ylabel('Idade', size=16)
plt.show()

# Trabalhando com histogramas => vamos visualizar como esta a distribuicao de frequencia dos dados
print('\nVamos antes de tudo fazer uma analise dos dados')
print(d.Age.describe())
d.Age.hist()
plt.title('Informacoes dos Passageiros do Titanic', size=18)
plt.xlabel('Idade', size=16)
plt.ylabel('Frequência Observada', size=16)
plt.show()

# Agora se quisermos salvar uma figura para um eventual relatorio ou artigo, podemos usar a instrucao abaixo >>= ela ira salvar a ultima figura => observe que ela deve ser inserida na estrutura da figura observada <=> plt.savefig()
d.Age.hist()
plt.title('Informacoes dos Passageiros do Titanic', size=18)
plt.xlabel('Idade', size=16)
plt.ylabel('Frequência Observada', size=16)
plt.savefig('D:\\Users\Angelo\AULAS\\HistTitanic.png')
plt.show()

# Vamos agora salvar a mesma figura com fundo transparente => observe
d.Age.hist()
plt.title('Informacoes dos Passageiros do Titanic', size=18)
plt.xlabel('Idade', size=16)
plt.ylabel('Frequência Observada', size=16)
plt.savefig('D:\\Users\Angelo\AULAS\\HistTitanicTransp.png', transparent=True)
plt.show()