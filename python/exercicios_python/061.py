'''Progressão aritmética com while (10 primeiros termos)'''
from time import sleep

num = int(input('Digite um número: ')) 
razao = int(input('Digite a razão: '))
contador = 1
progressao = num #Pode ser alterado

print('\033[33mCalculando...\033[0m')
sleep(1)

while contador <= 10:
    print(f'{progressao} → ', end='')
    progressao += razao #Faz a PA
    contador += 1 #Determina a duração do programa

print('Fim')