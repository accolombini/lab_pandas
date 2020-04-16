# Por dentro dos DataFrames => Combinando DataFrames e ampliando possibilidades de analise de dados
# Vamos criar 3 DataFrames e praticar => Ao trbalho!!!


import pandas as pd
import numpy as np

df1 = pd.DataFrame({'A' : ['A0', 'A1', 'A2', 'A3'],
                    'B' : ['B0', 'B1', 'B2', 'B3'],
                    'C' : ['C0', 'C1', 'C2', 'C3'],
                    'D' : ['D0', 'D1', 'D2', 'D3']},
                    index = [0, 1, 2, 3])

df2 = pd.DataFrame({'A' : ['A4', 'A5', 'A6', 'A7'],
                    'B' : ['B4', 'B5', 'B6', 'B7'],
                    'C' : ['C4', 'C5', 'C6', 'C7'],
                    'D' : ['D4', 'D5', 'D6', 'D7']},
                    index = [4, 5, 6, 7])

df3 = pd.DataFrame({'A' : ['A8', 'A9', 'A10', 'A11'],
                    'B' : ['B8', 'B9', 'B10', 'B11'],
                    'C' : ['C8', 'C9', 'C10', 'C11'],
                    'D' : ['D8', 'D9', 'D10', 'D11']},
                    index = [8, 9, 10, 11])

# Fazendo uma inspecao nos DataFrames
print('\nOs DataFrames para trabalho sao')
print('DataFrame numero 1')
print(df1)
print('\nDataFrame numero 2')
print(df2)
print('\nDataFrame numero 3')
print(df3)

# Primeira forma de concatenar
# Compondo um DataFrame a partir dos tres DataFrames iniciais >>= Concatenacao =>> observe que neste caso nossos DataFrames serão convertidos numa lista, o que pode não ser interessante <=> observe que so posso usar o metodo concat em uma lista, nao posso usa-lo diretamente em DataFrames
frames = [df1, df2, df3]
print('\n imprimindo todos os frames')
print(frames)
print('\nO tipo de dados de frames e: ', type(frames))

# Para resolver esse problema usamos da biblioteca pandas o metodo .concat() => com ele pegamos uma lista e convertemos para DataFrame, observe
# Nunca faca isso >>= framesCombinados = pd.concat(df1, df2, df3) <=> nao vai funcionar ok
framesCombinados = pd.concat(frames)
print('\nVamos agora imprimir o DataFrame1 combinado e depois visualizar seu tipo')
print(framesCombinados)
print('O Tipo de nosso novo DataFrame e: ', type(framesCombinados))

# Segunda forma de concatenar
# A forma mais elegante para se fazer isso e demonstrada abaixo >>= fique atento e nunca se esqueca do uso dos colchetes <=> o uso do colchetes ja subintende o objeto a ser concatenado
framesCombinados2 = pd.concat([df1, df2, df3])
print('\nVamos agora imprimir o DataFrame2 combinado e depois visualizar seu tipo')
print(framesCombinados2)
print('O Tipo de nosso novo DataFrame e: ', type(framesCombinados2))

# Vamos agora mergulhar mais fundo no processo de concatenacao ||> Acompanhe
grupo = pd.concat([df1, df2, df3])
# Imagine que voce quer algo mais => por algum motivo voce quer distinguir seus DataFrames |||> para isso, podemos usar as chaves e nelas especificar detalhes desejado para cada DataFrame =>> no caso chamarei cada um de f1, f2 e f3
grupo = pd.concat([df1, df2, df3], keys = ['f1', 'f2', 'f3'])
print('\nVamos observar o que muda em nossa concatenacao com o uso da diretiva keys')
print(grupo)

# Imagine agora que queremos exibir uma determinada coluna deste novo DataFrame >>= observe como e simples
print('\nImprimindo uma coluna especifica do DataFrame => que sera impresso a coluna A de todos os Frames')
print(grupo['A'])
# Agora queremos melhorar um pouco isso ||> vamos visualizar apenas o grupo 2 de nosso DataFrame |||> observe o uso do metodo .loc que fazra a localizacao do que deseja visualizar
print('\nVisualizando um grupo especifico do DataFrame')
print(grupo.loc['f2'])

# Terceira maneira de concatenar
# Neste caso faremos uso do metodo .append ||> primeiramente vamos concatenar por partes e depois vamos concatenar todos de uma so vez

g2 = df1.append(df2)
print('\nImprimindo o primeiro estagio de concatenacao com append')
print(g2)

g2.append(df3)
print('\n Completando o processo de concatencao')
print(g2.append(df3))

# Fazendo tudo de uma unica vez |||> observe
g4 = df1.append(df2).append(df3)
print('\nImprimindo concatencao completa usando .append')
print(g4)
