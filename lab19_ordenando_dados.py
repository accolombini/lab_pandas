# Nesta pratica nosso objetivo e continuar preparando os dados para analise, limpando e estruturando os dados que nao atendem ou podem que comprometer a qualidade dos resultados e assim ampliar nossa capacidade de analise >>= nao devemos perder de vista que estamos pensando em um volume muito grande dados =>> Big Data >>= E comum que dados estejam desordenados por algum motivo na coleta/armazenamento, por exemplo. Pode ser que para sua analise os dados ordenados sejam mais interessantes >>= E disso que estaremos falando nesta pratica
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


df = pd.DataFrame({'Col1' : ['A', 'A', 'B', np.nan, 'D', 'C'], 
                    'Col2' : [2, 1, 9, 8, 7, 4], 
                    'Col3' : [0, 1, 9, 4, 2, 3]
                    })

print('\nVisualizando nosso DataFrame')
print(df)

# Podemos ordenar de forma crescente ou forma decrescente usando o metodo .sort_values() que tem como default a ordenacao por linha (axis = 0) em forma crescente e exige que se entre com o by (no minimo) >>= Vamos praticar
print('\nOrdenando de forma crescente considerando by = Col1')
print(df.sort_values(by='Col1'))
print('\nOrdenando de forma crescente considerando by = Col2')
print(df.sort_values(by='Col2'))
print('\nOrdenando de forma crescente considerando by = Col3')
print(df.sort_values(by='Col3'))
# Podemos ordenar por multiplas colunas, neste caso o algoritmos e inteligente o bastante para classificar pela primeira coluna sinalizada e depois se houver possibilidades de rearanjos nas outras colunas ele executa tambem, mas sempre ira priorizar sua primeira opcao
print('\nOrdenando de forma crescente considerando by = multiplas colunas')
print(df.sort_values(by=['Col3', 'Col1']))
# Podemos usar a mesma funcao para ordenar de forma decrescente simplesmente alterando a digiretiva ascending para False >>= observe
print('\nOrdenando de forma decrescente considerando by = Col3')
print(df.sort_values(by='Col3', ascending=False))
print('\nOrdenando de forma decrescente considerando by = multiplas colunas')
print(df.sort_values(by=['Col3', 'Col1'], ascending=False))
