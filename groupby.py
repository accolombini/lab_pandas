# Por dentro dos DataFrames => Realizando merges  e explorando groupby e ampliando possibilidades de analise de dados
# Vamos criar nosso DataFrame e praticar => para pratica do metodo groupby <=> Ao trbalho!!!
# Observe a capacidade de filtrar e realizar operacoes por tras deste metodo


import pandas as pd
import numpy as np


# Para esta prática partiremos de estruturas do tipo DataFrame <=> construido diretamente
df = pd.DataFrame({'A' : ['verdadeiro', 'falso', 'verdadeiro', 'falso', 
                        'verdadeiro', 'falso', 'verdadeiro',   'falso'],
                    'B' : ['um', 'um', 'dois', 'tres', 'dois', 'dois', 'um', 'tres'],
                    'C' : np.random.randn(8),
                    'D' : np.random.randn(8)})

print('\nOlhando o DataFrame criado')
print(df)

# Como primeiro desafio vamos a partir da coluna A (dados categoricos) extrair a soma dos valores numericos das Colunas C e D <=> na verdade de todos os valores numericos da tabela ||> observe como e simples
soma_a = df.groupby(['A']).sum()
print('\nA soma categorica a partir da coluna A e')
print(soma_a)

media_a = df.groupby(['A']).mean()
print('\nA media sera dada por')
print(media_a)

soma_b = df.groupby(['B']).sum()
print('\nA soma categorica a partir da coluna B e')
print(soma_b)

# Agora vamos dar um passo mais interessante extrapolando o agrupamento para duas colunas =>> a partir dai você pode tudo
soma_ab = df.groupby(['A', 'B']).sum()
print('\nA soma categorica a partir das colunas categoricas A com B:')
print(soma_ab)
