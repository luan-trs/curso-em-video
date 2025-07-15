'''Gerenciar o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas
ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo será guardado em um dicionário
incluindo o total de gols durante o campeonato'''
jogador = {}

jogador['nome'] = str(input('Nome do Jogador: '))
jogador['gols'] = []
jogador['total'] = 0
for g in range(int(input(f'Quantas partidas {jogador['nome']} jogou? '))):
    jogador['gols'].append(int(input(f'  Quantos gols na partida {g}? ')))
    jogador['total'] += jogador['gols'][g]
print('-=-'*20)

print(jogador)
print('-=-'*20)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-'*20)

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')

for p in range(len(jogador['gols'])):
    print(f'  => Na partida {p}, fez {jogador["gols"][p]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')