'''Faça uma função chamada contador() que recebe 3 parâmetros: início, fim e passo e realize a contagem.
Seu programa tem que realizar 3 contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) contagem personalizada'''
from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo += 1
    if inicio > fim and passo > 0:
        passo *= -1
    print('-=-'*20)
    
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    for i in range(inicio, fim+1, passo):
        print(f'{i} → ', end='', flush=True)
        sleep(0.5)
    print('FIM')

contador(1, 10, 1)
contador(10, 0, 2)
print('-=-'*20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)