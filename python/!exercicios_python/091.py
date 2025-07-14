'''Crie um programa onde 4 jogadores jogam um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final, coloque o dicionário em ordem, sabendo que o
vencedor tirou o maior número no dado'''
from random import randint
from time import sleep

resultados = {}
print('\033[33mValores sorteados:')

#Gera, guarda e mostra os números dos dados de cada jogador
for i in range(4):
    resultados[f'jogador{i+1}'] = randint(1, 6)
    print(f'jogador{i+1} tirou {resultados[f'jogador{i+1}']} no dado.')
    sleep(0.5)

print('\033[0m', end='')
print('-=-'*15)
print(f'\033[36m === RANKING DOS JOGADORES ===')

#Transforma o dicionário em uma lista de tuplas
resultados = list(resultados.items())

#Guarda essas tuplas de forma decrescente utilizando o algoritmo de sorting do exercicio 80 (adaptado)
result_ordenado = []
for i in range(4):
    if i == 0 or resultados[i][1] < result_ordenado[-1][1]:
        result_ordenado.append(resultados[i])
    else:
        posicao = 0
        while posicao < len(result_ordenado):
            if resultados[i][1] >= result_ordenado[posicao][1]:
                result_ordenado.insert(posicao, resultados[i])
                break
            posicao += 1

#Transforma a lista de tuplas em um dicionario
ranking = dict(result_ordenado)

#Mostra os resultados do maior ao menor
pos = 1
for k, v in ranking.items():
    print(f'    {pos}º lugar: {k} com {v}.')
    pos += 1