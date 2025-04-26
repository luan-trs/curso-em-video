'''Programa que mostre o fatorial de um número'''
from time import sleep

num = int(input('Digite um valor: '))
contador = num
fatorial = 1

print(f'\033[35mCalculando fatorial de {num}...\033[0m')
sleep(1.5)

while contador != 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
  
print (f'\033[32m{fatorial}\033[0m')