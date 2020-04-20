# Nesta pratica nosso objetivo e continuar preparando os dados para analise, limpando e estruturando os dados que nao atendem ou podem comprometer a qualidade dos resultados e assim ampliar nossa capacidade de analise >>= nao devemos perder de vista que estamos pensando em um volume muito grande dados =>> Big Data >>= E comum que dados estejam faltando ou que estejam em nao conformidade por algum problema na coleta/armazenamento, por exemplo. Estes dados NaN podem ser tratados de varias formas e disso que falaremos nessa pratica.
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
datas = pd.date_range('20190101', periods=60, freq='D')
df = pd.DataFrame(np.random.randn(60,5), index=datas, columns=list('ABCDE'))

print('\nVamos visualizar nosso DataFrame df')
print(df.head(3))
print('\nQueremos agora visualizar a dimensao de nossos dados')
print('\n O DataFrame df: ', df.shape)
print('\nQueremos agora visualizar quais os tipos de dados')
print('\nO DataFrame df:')
print(df.dtypes)
# Vamos criar uma nova coluna, sendo que ela devera conter os dados da coluna A que sejam maiores que Zero =>> Vamos acompanhar <=> observe que algumas linhas serao preenchidas com NaN
df['F'] = df.A[df.A > 0]
print('\nVamos visulaizar a nova coluna')
print(df.head(4))
# A intencao foi propositalmente gerar esses NaN para que possamos fazer alguns exercicios com eles =>> para isso vamos fazer duas copias do DataFrame para realizarmos algumas manipulacoes
df2 = df.copy()
df3 = df.copy()
print('\nVisualizando as copias realizadas df2 e df3')
print(df2.head(3))
print(df3.head(3))

print('\nNossa primeira manipulacao e para remover os NaN da coluna F')
print('Observe que o uso do metodo .dropna() ira remover a linha interira que contenha um NaN')
print(df2.dropna())
print('\nPodemos visualizar o numero de linhas que foram removidas atraves de dropona():')
print(df2.dropna().shape)

# So para que possamos perceber a flexibilidade dos metodos a nossa disposicao, vamos agora usar o DataFrame df3 e ao inves de remover a linha com NaN, vamos substituir os NaN pela media dos dados da coluna A (poderia ser qualque outra coisa ok). Vamos fazer uso do metodo fillna() =>> observe
print('\nPreenchendo os dados NaN da coluna F com a media dos valores da coluna A')
print(df3.F.fillna(np.mean(df3.A)))
a = df3.F.fillna(np.mean(df3.A))
print('\nObserve que agora usaremos o .shape sem o parenteses, isso ocorre porque a nao e uma tupla')
print(a.shape)
print('\nPreenchendo os dados NaN de todo o DataFrame com a media dos valores da coluna A => veja como e simples')
print(df3.fillna(np.mean(df3.A)))
# Agora vamos criar um novo DataFrame e substituir os NaN por uma constante qualquer =>> acompanhe
df4 = df.copy()
print('\nSubstituindo NaN por uma constante')
print(df4.fillna(value=535))
