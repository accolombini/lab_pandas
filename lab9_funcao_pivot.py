# Nesta pratica nosso objetivo e transformar um tipo de dado em outro, ja praticamos isso antes, mas agora trataremos de forma especifica o assunto ||> vamos agora praticar reshapes mais elaborados >>= vamos trabalhar!!!


import pandas as pd
import numpy as np


dias = pd.date_range(start='20190101', periods=12)
print('\nA variavel dias gerada e do tipo: ', type(dias))
print(dias)
Pessoa = ['George', 'Victor', 'Lucas']
print('\nA variavel Pessoa gerada e do tipo: ', type(Pessoa))
print(Pessoa)
# O uso do metodo .choice() =>> que permite escolher um individuo no vetor analisado a partir de uma diretiva no caso estamos usando random
np.random.choice(Pessoa)
print('\nComo teste vamos visulaizar uma execucao aleatoria: ', np.random.choice(Pessoa))
# A seguir definimos duas variaveis do tipo listas iniciadas como listas vazias
Nome = []
Gasto = []
for i in range(12):
    Nome.append(np.random.choice(Pessoa))
    Gasto.append(np.round(np.random.rand() * 100, 2))
print('\nA estrutura gerada Nome e do tipo: ', type(Nome))
print(Nome)
print('\nA estrutura gerada Gasto e do tipo: ', type(Gasto))
print(Gasto)

# Vamos agora a partir das listas geradas criar um DataFrame >>= com isso estaremos agrupando todas as variaveis de trabalho
df = pd.DataFrame({'Dia' : dias, 'Nome' : Nome, 'Gasto' : Gasto})
print('\n A variavel DataFrame gerada e:')
print(df)

# Feito isso =>> imagine agora que nosso desafio seja organizar essa estrutra da seguinte forma ->> queremos saber por data quanto gastoru cada individuo naquele dias especifico >>= em outras palavras queremos um reshape que nos forneca |||> data | Nome1  | Nome2 | Nome3
#                                 | G1     | G2    | G3
cv = df.pivot(index='Dia', columns='Nome', values='Gasto')
print('\nVamos imprimir o controle de vendas usando o metodo .pivot()')
print(cv)
