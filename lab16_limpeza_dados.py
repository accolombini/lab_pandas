# Nesta pratica nosso objetivo o de preparar os dados para analise, limpando e estruturando os dados que nao atendem ou podem comprometer a qualidade dos resultados e assim ampliar nossa capacidade de analise >>= nao devemos perder de vista que estamos pensando em um volume muito grande dados =>> Big Data >>= vamos acompanhar
# Em se tratando de Big Data e IoT temos os 4 Vs >>= V => Volume V => Velocidade V => Variedade V => Veracidade
# Para uma limpeza adequada dos dados e uma consequente estruturacao devemos antes de tudo entender bem os dados que temos nas maos pense no seguinte para iniciar:
# 1 -> Saber qual o objetivo
# 2 -> Entra lixo sai lixo
# 3 -> Transformar os dados em estruturas: listas, tuplas, dicionarios, vetores, matrizes
# 4 -> Salvar em arquivos
# 5 -> Separar em diretorios
# Resumo [Dado] =>> [Estrutura] =>> [Arquivar ~> Salvar]


import pandas as pd
import numpy as np


# Vamos comecar nosos trabalhos sumarizando nossos dados =>> queremos saber o que temos
datas = pd.date_range('20200101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=datas, columns=['Var_A', 'Var_B', 'Var_C', 'Var_D'])
df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D' : np.array([3] * 4, dtype='int32'),
                    'E' : pd.Categorical(['test', 'train', 'test', 'train']),
                    'F' : 'Python'})

# Vamos inialmente visualizar os dados que temos - uma amostra
print('\nA variavel datas gerada para ser index:')
print(datas)
print('\nO DataFrame df:')
print(df)
print('\nO DataFrame df2:')
print(df2)
print('\nQueremos agora visualizar a dimensao de nossos dados')
print('\n O DataFrame df: ', df.shape)
print('\nQueremos agora visualizar quais os tipos de dados')
print('\nO DataFrame df2:')
print(df2.dtypes)
print('\nQueremos agora visualizar a dimensao de nossos dados')
print('\n O DataFrame df2: ', df2.shape)
print('\nQueremos agora visualizar quais os tipos de dados')
print('\nO DataFrame df2:')
print(df2.dtypes)

# Para dados numericos podemos usar ainda o metodo .describe() => observe que teremos uma primeira abordagem estatística descritiva dos dados
print('\nDescritivo dos dados numericos do DataFrame df')
print(df.describe())
print('\nDescritivo dos dados numericos do DataFrame df2')
print(df2.describe())

# Agora vamos a partir dos dados gerar um novo DataFrame (df1) que sera um subconjunto do DataFrame df => criaremos tambem uma nova coluna chamada Var_E <$> observe
df1 = df.reindex(index=datas[0:4], columns=list(df.columns) + ['Var_E'])
print('\nVisualizando o DataFrame df1 gerado')
print(df1)
# Atribuindo valores ao novo DataFrame (df1) na coluna Var_E
print('\nValores sendo atribuidos a coluna Var_E')
df1.loc[datas[0]:datas[1], 'Var_E'] = 77
print(df1)
print('\nQual o tipo de dados de df1')
print(df1.dtypes)
print('\nVamos aplicar .describe() para avaliar estatisticamente o novo DataFrame')
print(df1.describe())
