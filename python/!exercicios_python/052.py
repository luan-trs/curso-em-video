'''Numero primo ou não'''
num = int(input('Digite um valor: '))
acumu = 0

for c in range(1, num+1): # cria um contador
    div = num % c # divide o número pelo contador
    if div != 0:
        print(f'\033[;31m{c}\033[0m', end=' ') # se o número não for divisor, ele aparece em vermelho
    else:
        print(f'\033[;33m{c}\033[0m', end=' ') # se o número for divisor, ele aparece em amarelo
        acumu += 1 # conta quantos divisores o número tem


if acumu == 2 or num == 1:
    print(f'\n{num} foi divisível {acumu} vezes, ele é um número \033[;32mPRIMO\033[0m')
else:
    print(f'\nO número {num} foi divisível {acumu} vezes, ele \033[;31mNÃO É PRIMO\033[0m')
