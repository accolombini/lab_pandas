# Embora basico esse e um assunto muito importante no Python e apresenta uma serie incrivel de ferramentas prontas para manipular estruturas indexadas


import numpy as np
import pandas as pd


# Criando e manipulando listas
v = [22, 55, 7, 9]
print('\nTidpo de dados: ', type(v))
print('Imprimindo uma lista: ', v)
print('Acessando um elemento da lista, por exemplo v[2] => terceiro elemento ', v[2])
# Podemos indexar de tras para frente =>> pra isso usamos indices negativos e o ultimo elemento e referenciado por ||> -1 -> observe </> Atencao se usar um indice que extrapole os limites de sua lista tera uma mensagem de erro
print('Imprimindo o ultimo elemento da lista => v[-1]: ', v[-1])
print('Imprimindo o terceiro elemento de tras para frente => v[-3]: ', v[-3])

# Moleza ate aqui => vamos melhorar um pouco e trabalhar com indexacao multipla =>> pandas.MultiIndex >>= metodo que realiza indexacao multi-nivel ou hierarquica indexando objetos para objetos pandas
arrays = [[1, 1, 2, 2], ['red', 'blue', 'red', 'blue']]
print('\nQual o tipo de arrays: ', type(arrays))
# Vamos agora aplicar a transforamcacao MultiIndex => atento as mudancas
v = pd.MultiIndex.from_arrays(arrays, names= ('number', 'color'))
print('Qual o tipo de v => atento a transformacao: ', type(v))
print(v)
# Atencao nem sempre a transformacao sera perfeita como essa => pode ser que você precise trabalhar um pouco seus dados

# Melhorando um pouco mais isso vamos agora fazer o produto cartesiano usando =>> pandas.MultiIndex.from_product >>= vamos usar duas listas e realizar o produto cartesiano entre as listas usando o metodo pandas.MultiIndex_from_product ||> observe
numbers = [0, 1, 2]
colors = ['green', 'purple']
print('\nQual o tipo de numbers? ', type(numbers))
print('\nQual o tipo de colors? ', type(colors))
# O produto crtesiano esperado entre numbers e colors e =>> [0, green], [0, purple], [1, green], [1, purple], [2, green], [2, purple]
pc = pd.MultiIndex.from_product([numbers, colors], names=['number', 'color'])
print('\nO tipo da variavel pc apos uso de MultiIndex.from_product: ', type(pc))
print('O produto cartesiano de numbers x colors e')
print(pc)
