# Nesta pratica nosso objetivo e transformar um tipo de dado em outro, ja praticamos isso antes, mas agora trataremos de forma especifica o assunto ||> vamos agora praticar reshapes mais elaborados >>= vamos trabalhar!!!
# A caracteristica marcante do metodo pivot e o fato de nao admitir o uso de index repetidos => dados de igual valor </> Para resolver esse problema temos o metodo .pivot_table()


import pandas as pd
import numpy as np


Carros = [7, 4, 3, 2, 8]    # Numero de carros vendidos
dias = pd.date_range('20190101', '20190101', periods=5) # Vetor de dias inicio e fim no mesmo dia repetido 5 vezes
print('\nDias ', dias)
vendedor = ['George', 'Vagner', 'Pedro', 'Vagner', 'George'] # Vetor de vendedores
df = pd.DataFrame({'Vendas' : Carros, 'Data' : dias, 'Vendedor': vendedor}) # Numero de carros vendidos e vendedores

print('\nVams observar o DataFrame gerado')
print(df)

# Note que propositalmente nosso index (data) so possui valores repetidos >>= observe o que acontecera com o uso do metodo .pivot

# pd.pivot(df, index='Data', columns='Vendedor', values='Vendas') # Nao executa problemas com os indices
# Atencao note que o tipo de agregamento que e feito por default e a media dos valores que se repetem >>= lembre-se disso se quiser um resultado diferente
ptd = pd.pivot_table(df, index='Data', columns='Vendedor',values='Vendas')
print('\nObservando o uso do metodo .pivot_table')
print(ptd)
# Neste caso alteramos o valor default para sum => aggunc = sum
pts = pd.pivot_table(df, index='Data', columns='Vendedor',values='Vendas',aggfunc='sum')
print('\nObservando o uso do metodo .pivot_table')
print(pts)
