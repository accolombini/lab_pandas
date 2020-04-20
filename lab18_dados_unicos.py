# Nesta pratica nosso objetivo e continuar preparando os dados para analise, limpando e estruturando os dados que nao atendem ou podem que comprometer a qualidade dos resultados e assim ampliar nossa capacidade de analise >>= nao devemos perder de vista que estamos pensando em um volume muito grande dados =>> Big Data >>= E comum que dados estejam reetidos por algum problema na coleta/armazenamento, por exemplo. Estes dados repetidos podem ser tratados de varias formas e disso que falaremos nessa pratica.
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


df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D' : np.array([3] * 4, dtype='int32'),
                    'E' : pd.Categorical(['test', 'train', 'test', 'train']),
                    'F' : 'Python',
                    'G' : [2, 2, 4, 4],
                    'H' : [np.nan, 2, 4, np.nan]
                    })
print('\nVamos observar nosso DataFrame')
print(df2)

# Para saber se existem dados repetidos em um DataFrame exite um metodo especifico para esse fim .nunique() =>> se axis = 0 a busca sera por linhas caso axis = 1 a busca sera por colunas ==> Esse metodo pode considerar valores distintos de NaN -> basta usar a diretiva dropna = True que NaN nao sera contabilizado
print('\nVisualizando se ha dados repetidos no DataFrame')
print(df2.nunique())

# Agora vamos mudar a visualizacao dos dados => saindo do default
print('\nVamos agora analizar por colunas e considerar NaN na contagem')
print(df2.nunique(axis=1, dropna=False))
# Agora vamos mudar a visualizacao dos dados => saindo do default mas excluindo NaN (default)
print('\nVamos agora analizar por colunas e considerar NaN na contagem')
print(df2.nunique(axis=1, dropna=True))

# Vamos agora tratar as duplicatas
# Primeiramente vamos remover as duplicatas =>> importante quando nossa analise for impactada por dados repetidos
# Vamos inicialmente trabalhar com o metodo .drp_duplicates[] que por padrao mantem o primeiro valor encontrado e ira remover a/as duplicata(s) -> varre linhas por padrao se houver linha repetida aplica-se a regra, a menos que voce mude isso, vamos aos exemplos
print('\nEliminando as duplicatas .drop_diplicates() => nada sera removido, pois as linhas nao se repetem')
print(df2.drop_duplicates())
print('\nEliminando as duplicatas .drop_diplicates() => agora vamos analisar por subsets coluna G >>= observe')
print(df2.drop_duplicates(subset='G'))
print('\nEliminando as duplicatas .drop_diplicates() => vamos agora alem do subsets alterar o keep >>= observe')
print(df2.drop_duplicates(subset='G', keep='last'))
print('\nEliminando as duplicatas .drop_diplicates() => vamos agora alem do subsets alterar o keep para False >>= observe')
print(df2.drop_duplicates(subset='G', keep=False))
