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
print(f'\033[34m == RANKING DOS JOGADORES ==')

#Transforma o dicionário em uma lista de tuplas
result_desordenado = resultados.items() 

#Guarda essas tuplas de forma ordenada utilizando o algoritmo de sorting do exercicio 80 (adaptado)
result_ordenado = []
for i in range(4):
    if i == 0 or result_desordenado[i][1] > result_ordenado[-1][1]:
        result_desordenado[i].append(result_ordenado)
    else:
        posicao = 0
        while posicao < len(result_ordenado):
            if result_desordenado[i][1] <= result_ordenado[posicao][1]:
                result_ordenado.insert(posicao, result_desordenado[i])
                break
            posicao += 1

#Transforma a lista de tuplas em um dicionario
ranking = dict(result_ordenado)
for k, v in ranking.items():
    for i in range(4):
        print(f' {i+1}º lugar: {k} com {v}.')