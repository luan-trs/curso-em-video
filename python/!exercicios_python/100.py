'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
a soma entre todos os valores PARES sorteados pela função anterior'''
from random import randint
from time import sleep
numeros = []

def sorteia(lista):
    print('Sorteando 5 valores para a lista... ', end='')
    for i in range(5):
        n = randint(1, 10)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
        lista.append(n)
    print('FIM')
def somaPar(lista):
    soma = 0
    for n in lista:
        if n%2 == 0:
            soma += n
    print(f'Somando os valores pares de {lista}, temos {soma}')

sorteia(numeros)
somaPar(numeros)