# Nesta pratica nosso objetivo e aplicar os conhecimentos adquiridos e treinar nossa capacidade de analise
# => lembrando que podemos estar falando de arquivos gigantescos
# Em se tratando de Big Data e IoT temos os 4 Vs >>= V => Volume V => Velocidade V => Variedade V => Veracidade
# Os principais tipos de arquivos que iremos trabalhar sao: .txt, .csv e .xlx
# Arquivos .txt => normalmente empregados para informacoes nao estruturadas
# Arquivos .csv => sao os mais comuns encontrados por ai
# Arquivos .xlsx => sao arquivos do Excel
# Resumo [Dado] =>> [Estrutura] =>> [Arquivar ~> Salvar]


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Vamos carregar os dados que serao analisados =>> no caso os dados do Titanic que estao no formato .csv
d = pd.read_csv('D:\\Users\Angelo\AULAS\\titanic_train.csv')
# Fazendo uma rapida inspecao nos dados temos
print('\nInspecao inicial nos dados')
print(d.head(3))
print('\nA dimensao do arquivo de treino')
print(d.shape)
print('\nUma primeira inspecao atraves da estatistica descritiva')
print(d.describe())
# Dando continuidade aos estudos, vamos fazer algumas exploracoes dos dados => mulheres
womem = d.loc[d.Sex == 'female']['Survived']
print('\nMulheres que sobreviveram')
print(womem.sum())
rate_womem = sum(womem)/len(womem)
print('\nTaxa de mulheres que sobrevieram: ', rate_womem)
so_womem = (d.Sex == 'female').sum()
print('\nQuantidade de mulheres: ', so_womem)
# Dando continuidade aos estudos, vamos fazer algumas exploracoes dos dados => Homens
men = d.loc[d.Sex == 'male']['Survived']
print('\nHomens que sobreviveram')
print(men.sum())
rate_men = sum(men)/len(men)
print('\nTaxa de Homens que sobrevieram: ', rate_men)
so_men = (d.Sex == 'male').sum()
print('\nQuantidade de homens: ', so_men)
