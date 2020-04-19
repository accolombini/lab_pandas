# Nesta pratica nosso objetivo e continuar no processo de transformar um tipo de dado em outro, ja praticamos isso antes, mas agora trataremos de forma especifica o assunto ||> vamos agora praticar reshapes mais elaborados >>= vamos trabalhar!!!
# Nosso objetivo aqui e trabalhar com o metodo melt ||> fundir / juntar / agrupar <=> acompanhe


import pandas as pd


# Iniciamos com a variavel data sendo do tipo dicionario ||> acompanhe
data = {
    'Localizacao' : ['CidadeA', 'CidadeB'],
    'Temperatura' : ['Prevista', 'Atual'],
    'Set-2019' : [30, 32],
    'Out-2019' : [45, 43],
    'Nov-2019' : [24, 22]
}
print('\nVamos ver nossa variavel data')
print(data)
# Vamos agora no nosso primeiro Reshape transformar nossa variavel data em um DataFrame mais interessante de se visualizar => observe que com essa transformacao voce conseguiu uma serie temporal que e nosso objetivo
df = pd.DataFrame(data, columns=['Localizacao','Temperatura',  'Set-2019', 'Out-2019', 'Nov-2019'])
print('\nVamos ver como ficou nosso DataFrame')
print(df)
# Vamos melhorar um pouco nosso processo de analise ||> usaremos o melt para fundir Localizacao com Temperatura =>> acompanhe
df2 = pd.melt(df, id_vars=['Localizacao', 'Temperatura'], var_name='Data', value_name='Valor')
print('\nVisualizando nosso primeiro melt')
print(df2)
