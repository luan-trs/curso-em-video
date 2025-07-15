'''Aprimore o exercício 93 para que ele funcione com vários jogadores, incluindo um sistema de visualiuzação
de detalhes de aproveitamento de cada jogador'''
jogadores = []
jogador = {}

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    jogador['gols'] = []
    for g in range(int(input(f'Quantas partidas {jogador['nome']} jogou? '))):
        jogador['gols'].append(int(input(f'  Quantos gols na partida {g+1}? ')))
    jogador['total'] = sum(jogador['gols'])
    jogadores.append(jogador.copy())

    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if continuar in 'SN':
            break
        print('\033[41mERRO!\033[0m Responda apenas S ou N.')
    if continuar == 'N':
        break

print('-=-'*20)
print('cod  ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('---'*20)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('---'*20)

while True:
    index = int(input('\033[33mMostrar os dados de qual jogador? (999 para parar)\033[0m '))
    if index == 999:
        break
    if index >= len(jogadores):
        print(f'\033[31mERRO! Não existe jogador com o código {index}.\033[0m')
    else:
        print(f'\033[43m--- LEVANTAMENTO DO JOGADOR {jogadores[index]["nome"]}:\033[0m')
        for i, j in enumerate(jogadores[index]['gols']):
            print(f'    No jogo {i+1} fez {j} gols.')
print('\033[41m<< PROGRAMA ENCERRADO >>\033[0m')