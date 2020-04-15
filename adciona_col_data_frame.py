# Por dentro dos DataFrames => adicionando colunas


import pandas as pd
import numpy as np 

datas = pd.date_range('20190101', periods = 60, freq='D')
df = pd.DataFrame(np.random.randn(60, 5), index = datas, columns = list('ABCDE'))

# Vamos ver como ficou nosso DataFrame => observe que estamos usando com index nossa estrutura datas =>> que sabemos e do tipo DataIndex

print('\n', df)

print('\nQueremos apenas saber a dimensao da estrutura do nosso DataFrame, observe: ', df.shape)

# Nosso objetivo agora e adicionar uma coluna ao DataFrame =>> antes vamos olhar para sua estrutura usando .head()
print(df.head(3))
# Sao muitas as formas de adiconar uma coluna ao DataFrame, vamos ver algumas aqui ->> neste caso vamos simplesmente criar a coluna F e adicionar o valor 1 em todas as suas linhas, observe:
df['F'] = 1
print(df.head())
# E importante que ao adiconar uma nova coluna respeite o numero de linhas de seu DataFrame, caso contrario tera uma mensagem de erro. Neste caso, vamos usar a funcao range() para peencher todas as linhas
df['G'] = range(60)
print(df.head(8))
# Nosso desafio agora sera criar uma nova coluna realizando alguma operacao =>> neste exemplo faremos o produto da coluna A pela coluna B <=> elemento a elemento, veja como é simples
df['PRODUTO_AB'] = df['A'] * df['B']
print(df.head(20))
# A seguir vamos fazer uma edicao em uma das colunas de nosso DataFrame
df['G'] = 100
print(df.head(10))
