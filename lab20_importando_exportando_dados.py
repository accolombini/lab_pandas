# Nesta pratica nosso objetivo e importar e manipular arquivos que contenham os dados a serem analisados => lembrando que podemos estaar falando de arquivos gigantescos
# Em se tratando de Big Data e IoT temos os 4 Vs >>= V => Volume V => Velocidade V => Variedade V => Veracidade
# Os principais tipos de arquivos que iremos trabalhar sao: .txt, .csv e .xlx
# Arquivos .txt => normalmente empregados para informacoes nao estruturadas
# Arquivos .csv => sao os mais comuns encontrados por ai
# Arquivos .xlsx => sao arquivos do Excel
# Resumo [Dado] =>> [Estrutura] =>> [Arquivar ~> Salvar]


import pandas as pd
import numpy as np


# Importando e exportando dados >>= manipulando arquivos com Python
# Neste primeiro momento queremos carregar uma arquivo do tipo .dat (diferente dos anteriores convencionais)
d = pd.read_csv('D:\\Users\Angelo\AULAS\iris.data')
print('\nVamos visualizar o que temos em nosso arquivo')
print(d.head(4))
print('\nVisualizando o volume de dados: ', d.shape)
print('\nVisualizando o tipo de dados => observe que ele ira nos trazer a primeira linha como titulo das colunas, mas voce ja sabe que isso pode ser alterado')
print(d.dtypes)
print('\nVamos agora fazer uma primeira analise estatisica em cima dos dados =>> usando o metodo .describe()')
print(d.describe())

# Agora vamos a partir de dados do Excel exporta-los para .csv
d1 = pd.read_excel('D:\\Users\Angelo\AULAS\Data_03.xlsx')
print('\nVamos visualizar o que temos em nosso arquivo')
print(d1.head(4))
print('\nVisualizando o volume de dados Excel: ', d1.shape)
print('\nVisualizando o tipo de dados => olhando a tabela Excel')
print(d1.dtypes)
print('\nVamos agora fazer uma primeira analise estatisica em cima dos dados =>> usando o metodo .describe()')
print(d1.describe())
print('\nVamos ver nossa planilha Excel carregada usando a biblioteca Pandas => qual sera seu tipo de dado?')
print('Resposta  DataFrame =>>', type(d1))

# Vamos agora transformar nossos dados xlsx para .csv  =>> lembre-se que voce tem agora um documento do tipo DataFrame
print('\nPara converter um DataFrame para putro tipo de dado => use nomeDataFrame.to_tipodesejado, => observe')
print('Neste caso estaremos exportando para .csv =>> d1.to_csv("onde salvar")')
d1.to_csv('D:\\Users\Angelo\AULAS\DataConv_03.csv')
