# Por dentro dos DataFrames => algumas formas de visualizacao do DataFrame
# Atencao a estas dicas 


import pandas as pd
import numpy as np 
series = pd.Series([7, 4, 2, np.nan, 6, 9])
print('Impmrime o DataFrame Series: ')
print(series)
print('\nQual o tipo de dados de series? ', type(series))
# Gerando dadtas com pandas definindo a frequencia => periods = 6 <-> por default periodo será contado em dias
datas = pd.date_range('20180101', periods=6, freq='D')
print('\nDatas geradas:')
print(datas)
print('\nQual o tipo da estrutura datas: ', type(datas))
# Vamos agora criar um DataFrame para iniciar os estudos -> faremos uso do metodo random.randn() gerador de numeros aleatorios dentro de uma distribuicao normal com media zero e desvio padrao igual a 1 e vamos usar como index as datas geradas acima >>= observe
df = pd.DataFrame(np.random.randn(6, 4), index = datas, columns =list('ABCD')) # ['Carros', 'Paises', 'Pessoas', 'Python']
print('\nOlhando nosso DataFrame')
print(df)
print('\nAnalisando o tipo de nossa estrutura df: ', type(df))
# Agora vamos criar DataFrame de outra forma => usando dicionario e fazendo um mix de varios tipos de dados
df2 = pd.DataFrame({'A': 7, 'B': pd.Timestamp('20190101'), 'C': pd.Series(1, index=list(range(4)), dtype = 'float32'), 'D': np.array([3] * 4, dtype = 'int32'), 'E': pd.Categorical(['test', 'train', 'test', 'train']), 'F': 'Python'})
print('\nComo ficou nosso df2 >>= Observe que o Python prenche para nos todos os campos')
print(df2)
# Agorra queremos saber quais sao os tipos de dados que compoem nosso DataFrame
print('\nOs dados que compoem o DataFrame sao') 
print(df2.dtypes)

# Vamos agora aproveitar os DataFrames criados e estudar algumas formas praticas de visualizacao, lembrando que em big data estaremos trabalhando com DatFrames gigantescos

# Primeiramente =>> Vamos observar o head() e o tail() do DataFrame
print('\nVisualizando as duas primeiras linhas do DataFrame: ', df.head(2))
print('\nVisualizando as dua ultimas linhas do DataFrame: ', df.tail(2))

# Segundo =>> Como podemos visualizar os indices de referencia de nosso DataFrame
print('\nPara observar os index de nosso DataFrame: ')
print(df.index)

# Terceiro =>> Como podemos inspecionar as colunas do nosso DataFrame
print('\nAs colunas do DataFrame sob analise: ')
print(df.columns)

# Quarto =>> Atribuir as colunas ao uma variavel
c = df.columns
print('\nA variavel que armazena as colunas do DataFrame:')
print(c)

# Quinto =>> Vamos extrair do DataFrame apenas os valores numericos -> queremos deixar de fora as colunas e os index >>= transformando o DataFrame num array numpy
print('\nPegando a parte numerica de um DataFrame e transformando num array. Atencao ao uso do parenteses')
print('DataFrame df transformado em array numpy')
print(df.to_numpy())
print('DataFrame df2 transformado em array numpy')
print('\n', df2.to_numpy())

# Sexto =>> Obtendo a trasnposta de uma matriz (DataFrame)
print('\nObtendo a transposta dos conjuntos de dados df e df2')
print(df.T)
print('\n', df2.T)
