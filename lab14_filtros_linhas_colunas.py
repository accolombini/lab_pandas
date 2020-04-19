# Nesta pratica nosso objetivo e trabalhar com filtros de linhas e colunas de forma a ampliar nossa capacidade de manipulacao dos dados >>= nao devemos perder de vista que estamos pensando em um volume muito grande dados =>> Big Data >>= vamos fazer alguns slices observe
# Nosso objetivo aqui e trabalhar com filtros de linhas e colunas ||> na proxima pratica trabalharemos com filtros booleanos ~~> acompanhe

import pandas as pd
import numpy as np


datas = pd.date_range('20180101', periods=600, freq='D')
print('\nVariavel datas criada')
print(datas)
df = pd.DataFrame(np.random.randn(600,5), index=datas, columns=list('ABCDE'))
print('\nDataFrame criado')
print(df)
print('Dimensoes do data frame ', df.shape)
print('Vamos visualizar os ultimos elementos de nosso DataFrame')
print(df.tail())

# Imagine que nosso objetivo seja conseguir todos os elementos da Coluna D ~~> observe
print('\nVamos visulizar apenas os elementos da Coluna D')
print(df['D'])
print(df['D'].head())

# Ok aprendemos manipular colunas >>= nosso proximo desafio sera extrair um certo numero de linhas selecionadas slice ||> observe lembre-se que Python e nao inclusivo portanto o ultimo indice nao sera extraido
print('\nVamos extrair da linha 1 a linha 4 ~~> observe [1:5]')
print(df[1:5])

# Nosso proximo desafio sera a extracao de multiplas colunas ||> no caso as colunas B C D => observe o uso do metodo .loc() de localizacao |||> neste caso vamos extrair todas as linhas, mas voce podera explorar mais esse recurso

print('\nExtraindo as colunas B, C, D |> atento ao uso dos colchetes []')
print(df.loc[:, ['B', 'C', 'D']])
# Vamos agora selecionar apenas as 10 primeiras linas
print('\nExtraindo as colunas A, E |> extraindo as 10 primeiras linhas')
print(df.loc['20180101': '20180110', ['A', 'E']])

# Vamos agora selecionar apenas as 10 primeiras linas e atribuir a uma variavel para que possamos usar a funcao len()
f = df.loc['20180101': '20180110', ['A', 'E']]
print('\nExtraindo as colunas A, E |> extraindo as 10 primeiras linhas => obsrvando quanto temos de intervalo')
print(len(f))

# Agora vamos elevar um pouco o nivel de nossos filtros ||> muito importante acompanhe
# Vamos selecionar uma linha especfica e para isso usaremos o metodo .iloc ||> observe
print('\nVamos selecionar uma linha especficia (linha 480) do nosso DataFrame ~~> uso do .iloc')
print(df.iloc[480])

# Agora vamos fazer o fatiamente slice de linhas e colunas usando o .iloc >>= observe
print('\nPara nosso teste queremos extrair das linhas 2 a 4 e as duas primeiras colunas => observe o indice das colunas lembre-se do nao inclusivo')
print(df.iloc[2:4, 0:2])

# Agora nosso desfio e pegar um conjunto de dados especificos dentro de nosso DataFrame </> como podemos fazer isso??? <$> acompanhe
print('\nObserve como trabalhamos os []s neste exercicio => aqui estamos definindo exatamente o que queremos')
print(df.iloc[[1, 5, 9], [0, 3]])
print('\nNeste exemplo queremos definir as linas (intervalo) e vamos selecionar todas as colunas')
print(df.iloc[1:3, :])
