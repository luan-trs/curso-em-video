'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso. '''
from time import sleep

user = 0
while user != 5:
    num1 = int(input('Primeiro numero: '))
    num2 = int(input('Segundo numero: '))
    print('\033[33m-=-'*15)
    print('''1-Somar\n2-Multiplicar\n3-Maior numero\n4-Novos numeros\n5-Sair''')
    print('\033[33m-=-\033[0m'*15)
    user = int(input('Qual ação deseja fazer? '))

    if user == 1:
        print(f'\033[34mA soma dos números é: {num1+num2}\033[0m')

    elif user == 2:
        print(f'\033[34mO produto dos números é: {num1*num2}\033[0m')

    elif user == 3:
        if num1 > num2:
            print(f'\033[34mO maior número é: {num1}\033[0m')
        elif num2 > num1:
            print(f'\033[34mO maior número é: {num2}\033[0m')
        else:
            print('\033[34mOs dois números são iguais\033[0m')
    elif user == 4:
        print('\033[34m-=-Escolha os novos números-=-\033[0m')
    sleep(1.5)
        
        
print('\033[31mFim!\033[0m')


