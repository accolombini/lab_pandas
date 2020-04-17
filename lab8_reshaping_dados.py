# Nesta pratica nosso objetivo e transformar um tipo de dado em outro, ja praticamos isso antes, mas agora trataremos de forma especifica o assunto ||> acompanhe


import pandas as pd
import numpy as np


datas = pd.date_range('20200101', periods=6)
print('\nVamos avaliar qual o tipo de dados de datas: ', type(datas))
df = pd.DataFrame(np.random.randn(6, 4), index=datas, columns=['Var_A', 'Var_B', 'Var_C', 'Var_D'])
print('Vamos ver nosso DataFrame')
print(df)

# Vamos comecar com os processos de reshaping
# Primeiro vamos transpor nossos dados uso do .T
dft = df.T
print('\nO valor transposto de DataFrame => df.T')
print(dft)
# Para visualizar o shape de uma estrutura de dados usamos =>> nome_est.shape  <=> nao tem parenteses
print('\nO shape de nossa estrutura de dados df e: ', df.shape)
print('O shape de nossa estrutura de dados dft e: ', dft.shape)

# Segundo => vamos extrair de um DataFrame os valores numericos ->> uso do atributo .values <-> sem parenteses >>= observe que os dados resultantes serao do tipo numpy.ndarray

print('\nSo numeros do DataFrame dft')
print(dft.values)
print('\nO tipo de dado apos o de .values e: ', type(dft.values))

# Imagine que queiramos saber quantos elementos existem no nosso array =>> para isso vamos usar o metodo .size() ||> observe e imagine voce trabalhando com big data
print('\nQual o numero de elementos de nosso array: ', np.size(dft.values))

# Terceiro esse tipo de dado resultado do uso do .values pode ser atribuido a uma nova variavel => observe
v = dft.values

# Quarto podemos fazer um reshape a partir do dado gerado atraves do uso de .values >>= observe ||> fique atento que voce so podera fazer uso de valores que exatamente o seu numero de dados -> no caso usei 2x12 = 24, portanto ok 3x15, por exemplo, daria erro
r = v.reshape((2, 12))
print('\nA nossa variavel reshape de v (2, 12)')
print(r)
