# Nesta pratica nosso objetivo e transformar um tipo de dado em outro, ja praticamos isso antes, mas agora trataremos de forma especifica o assunto ||> vamos agora praticar reshapes mais elaborados >>= vamos trabalhar!!!
# Nosso objetivo aqui e trabalhar com pilhas de dados ||> acompanhe


import pandas as pd
import numpy as np


# Observe que neste caso estaremos fazendo uma leitura de um arquivo .csv diretamente da internet => observe
df = pd.read_csv('https://media.geeksforgeeks.org/wp-content/uploads/nba.csv')
print('\nOlhando para o arquivo csv extraido diretamente da internet')
print(df.head(20))
# Queremos agora saber a forma desses lados => sua dimensão
print('\nA dimensao deste arquivo e: ', df.shape)

# Dado que temos uma panorama dos dados queremos agora fazer um Rehsape para facilitar nosso trabalho => vamos fazer uso do stack </> observe que estaremos empilhando os dados, neste caso as colunas estarao sendo convertidas em linhas

stack_df = df.stack()
print('\nVamos agora visualizar nosso reshape')
print(stack_df)

# Para eu retornar a tabela original basta usar o mpdulo unstack >>= observe

udf = stack_df.unstack()

print('\nVamos agora visualizar nossa tabela e conferir com a original')
print(udf.head(3))
