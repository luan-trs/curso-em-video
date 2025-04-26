#Faça um programa que jogue par ou ímpar. O jogo será interrompido quando o usuario perder
#Mostre o total de vitórias consecutivas que ele conquistou
from random import randint

result = 0
vitorias = 0

print('-=-'*10)
print('PAR OU ÍMPAR')

while True:
    print('-=-'*10)
    user = int(input('Digite um valor: '))
    computador = randint(0, 10)
    escolha = input('Você escolhe par ou ímpar?[p/i] ').lower()

    print('-'*15)
    if (computador+user)%2 == 0:
        result = 'p'
    else:
        result = 'i'
    print(f'Usuário: {user} | Computador: {computador} | {user+computador} é {'par' if result == 'p' else 'ímpar'}')
    print('-'*15)
    
    if escolha == result:
        print('\033[32mVOCÊ VENCEU!\033[0m')
        vitorias += 1
        print('Vamos jogar novamente!')
    else:
        break

print('\033[31mGAME OVER\033[0m')
print(f'Você perdeu com {vitorias} vitórias consecutivas')
    