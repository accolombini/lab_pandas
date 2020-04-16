# Por dentro dos DataFrames => Realizando merges e ampliando possibilidades de analise de dados
# Vamos criar 3 DataFrames e praticar => para pratica do metodo Merge <=> Ao trbalho!!!


import pandas as pd
import numpy as np


# Para esta prática partiremos de estruturas do tipo dicionarios e converteremos para DataFrame para expandir nossas possibilidades de analises
# Cadastro da loja a
cadastro_a = {'Id' : ['AA2930', 'BB4563', 'CC2139', 'DE2521', 'GT3462', 'HH1158'],
            'Nome' : ['Victor', 'Amanda', 'Bruna', 'Carlos', 'Ricardo', 'Maria'],
            'Idade' : [20, 35, 40, 54, 30, 27],
            'CEP' : ['00092-029', '11111-111', '22222-888', '00000-999', '88888-111', '77777-666']
            }
print('\nVamos primeiro visualizar o tipo ', type(cadastro_a))
cadastro_a = pd.DataFrame(cadastro_a, columns = ['Id', 'Nome', 'Idade', 'CEP'])
print('Vamos ver nosso primeiro DataFrame cadastro_a')
print(cadastro_a)

# Cadastro da loja b
cadastro_b = {'Id' : ['CC9999', 'EE4488', 'DD9999', 'GT3462', 'HH1158'],
            'Nome' : ['Marcos', 'Patricia', 'Erika', 'Ricardo', 'Maria'],
            'Idade' : [19, 30, 22, 30, 27],
            'CEP' : ['00092-029', '11111-111', '11111-888', '88888-111', '77777-666']
            }
print('\nVamos primeiro visualizar o tipo ', type(cadastro_b))
cadastro_b = pd.DataFrame(cadastro_b, columns = ['Id', 'Nome', 'Idade', 'CEP'])
print('Vamos ver nosso segundo DataFrame cadastro_b')
print(cadastro_b)

# Cadastro da loja c
compras =  {'Id' : ['AA2930', 'EF4488', 'CC2139', 'EF4488', 'CC9999', 'AA2930', 'HH1158', 'HH1158'],
            'Data' : ['2019-01-01', '2019-01-30', '2019-01-30', '2019-02-01', '2019-02-20', '2019-03-15', '2019-04-01', '2019-04-10'],
            'Valor' : [200, 100, 40, 150, 300, 25, 50, 500],
            }
print('\nVamos primeiro visualizar o tipo ', type(compras))
compras = pd.DataFrame(compras, columns = ['Id', 'Data', 'Valor'])
print('Vamos ver nosso DataFrame compras')
print(compras)

# Vamos agora realizar estudos sobre esses DataFrames fazendo uso do metodo Merge >>= esta e uma pratica estrutural => estamos preparando os dados |> a seguir a sintaxe de uso do metodo merge da biblioteca Pandas
# pd.merge(tabela_da_equerda, tabela_da_direita, on = 'coluna_coincidente', how = 'left|righ|inner|outer')
# inner join =>> pega a interseccao entre duas tabelas
# full join =>> pega as duas tabelas ||> estou interessado em juntar as duas tabelas
# left join =>> pega a tabela da esquerda e sua interseccao com a tabela da direita |> na verdade pega a tabela da esquerda full
# right join =>> pega a tabela da direita e sua interseccao com a tabela da esquerda |. na verdade pega a tabela da direita full

# Comecando com INNER JOIN =>> como desafio queremos verificar os clientes da loja_a que também sao clientes da loja_b ||> portanto, estamos interessados na interseccao de da loja_a com a loja_b

print('\nNosso primeiro merge => inner join entre cadastro_a e cadastro_b => observe que a diretiva x diz respeito a tabela da esquerda e a diretiva Y diz respeito a tabela da direita')
print(pd.merge(cadastro_a, cadastro_b, how = 'inner', on = ['Id']))

print('\nNosso segundo desafio e um filtro mais especifico, queremos identificar exatamente o que trazer no nosso merge ||> observe que nosso filtro se aplica a tabela da direita tabela representada por y observe tambem o uso de Id verifique o que acontece se altera-lo')
print(pd.merge(cadastro_a, cadastro_b[['Id', 'Idade', 'CEP']], on = ['Id'], how = 'inner'))

# Podemostambém alterar o sufixo de nosso merge </> imagine que queremos substituir o sufixo x e o sufixo y
print('\nNosso terceiro desafio e alterar o sulfixo de nossas tabelas |> basta adicionar a diretiva suffixes')
print(pd.merge(cadastro_a, cadastro_b[['Id', 'Idade', 'CEP']], on = ['Id'], how = 'inner', suffixes = ('_A', '_B')))

# Agora vamos trabalhar com o FULL JOIN
# A forma mais simples de realizar o FULL JOIN e atraves do .concat() ja estudado ||> teremos a pendência de eliminar as duplicatas, mas isso sera um proximo desafio

print('\nRealizando o FULL JOIN com o .concat()')
print(pd.concat([cadastro_a, cadastro_b], ignore_index = True))

# Eliminando as duplicatas |> siga os passos
lojas = pd.concat([cadastro_a, cadastro_b], ignore_index = True)
print('\nEliminando duplicatas')
clientes_unicos = lojas.drop_duplicates(subset = 'Id')
print(clientes_unicos)

# Vamos agora realizar um LEFT JOIN
# Nosso desafio agora sera pegar alguma informacao da tabela compras e passar para cadastro_a ||> acompanhe neste exemplo queremos saber quais clientes que realizaram compras e se encontram cadastrados na loja_a >>= cadastro_a vamos usar como identificador o Id

print('\nClientes que fizeram compras e que estao cadastrados na loja_a')
esquerda = pd.merge(cadastro_a, compras, how = 'left', on = ['Id'])
print(esquerda)
print('\nPara facilitar o entendimento vamos exibir as tabelas A e Compras')
print('\nLoja_A')
print(cadastro_a)
print('\nCompras')
print(compras)

# Como exrcicio vamos fazer uso do metodo groupby() e aplicar uma operacao ha um filtro atraves do Merge ||> mais facil fazer que falar => acompanhe

soma = esquerda.groupby(['Id', 'Nome'])['Valor'].sum()
print('\nA soma de "Valor" e')
print(soma)

# Vamos agora fazer merges de dados OUTER =>> Junta dois conjuntos e atribui tudo a um novo DataFrame ||> observe o NaN e tambem as repeticoes

out = pd.merge(cadastro_a, cadastro_b, how='outer', on=['Id'])
print('\nO valor de out =>> resultado do merge com a diretiva how = outer')
print(out)

# Podemos agora fazer uso da diretiva ->> indicator||> que nos mostra em qual tabela esta a referencia, observe

out_ind = pd.merge(cadastro_a, cadastro_b, how='outer', on=['Id'], indicator=True)
print('\nDiretiva how outer com a diretiva indicator ||> observe')
print(out_ind)
