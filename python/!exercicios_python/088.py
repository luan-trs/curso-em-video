'''Faça um programa que ajude um jogador da mega sena a criar palpites.
Perguntar quantos jogos serão feitos e sortear 6 números entre 1 e 60 para cada jogo, cadastrando em uma matriz'''
from random import randint
resultados = []
jogo = []
print('\033[32m-=-=-=-=- MEGA SENA -=-=-=-=-\033[0m')
jogos = int(input('Quantos jogos deseja gerar? '))

print('\033[33m')
for i in range(jogos):
    for j in range(6):
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
        else:
            num = randint(1, 60)
            jogo.append(num)
    resultados.append(jogo[:])
    jogo.clear()

    print(f'JOGO {i+1}: {resultados[i]}')
print('\033[34m-=-=-=-= BOA SORTE =-=-=-=-=-\033[0m')