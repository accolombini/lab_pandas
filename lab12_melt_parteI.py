# Nesta pratica nosso objetivo e continuar no processo de transformar um tipo de dado em outro, ja praticamos isso antes, mas agora trataremos de forma especifica o assunto ||> vamos agora praticar reshapes mais elaborados >>= vamos trabalhar!!!
# Nosso objetivo aqui e trabalhar com o metodo melt ||> fundir / juntar / agrupar <=> acompanhe


import pandas as pd


df = pd.DataFrame({'A' : {0 : 'a', 1 : 'b', 2 : 'c'},
                    'B' : {0 : 1, 1 : 3, 2: 5},
                    'C' : {0 : 2, 1 : 4, 2 : 6}})

print('\nVamos visualizar o Dataframe criado')
print(df)

# Neste exemplo do melt vamos fundir a coluna A com a coluna B =>> observe a estrutura utilizada e o resultado =>> note que a juncao entre A e B e feita em cima dos valores ||> observe
fab = pd.melt(df, id_vars=['A'], value_vars=['B'])
print('\nComo ficou nosso primeiro melt')
print(fab)
# Este exemplo e so para mostrar que o uso do [] e opcional => observe =>> note que a juncao entre A e B e feita em cima dos valores ||> observe
fab2 = pd.melt(df, id_vars='A', value_vars='B')
print('\nComo ficou nosso segundo melt')
print(fab2)
# No exemplo a seguir vamos fundir a variavel C tambem ||> observe que neste caso precisamos manter o [] =>> preste atencao em como foi realizado a juncao da variavel A com B e C, em outras palavras as variaveis B e C estarao indexadas com a variavel A
fabc = pd.melt(df, id_vars='A', value_vars=['B', 'C'])
print('\nComo ficou nosso terceiro melt')
print(fabc)
# Agora aproveitando que estamos em processo de Reshape vamos alterar os nomes das colunas (variable) para uma condicao mais atrativa =>> oberve como e simples
fabcn = pd.melt(df, id_vars='A', value_vars=['B', 'C'], var_name='Novo_Nome')
print('\nComo ficou nosso quarto melt')
print(fabcn)
# Agora aproveitando que estamos em processo de Reshape vamos alterar os nomes das colunas (variable) e (value) para uma condicao mais atrativa =>> oberve como e simples
fabcnn = pd.melt(df, id_vars='A', value_vars=['B', 'C'], var_name='Novo_Nome', value_name='Col_var')
print('\nComo ficou nosso quarto melt')
print(fabcnn)
