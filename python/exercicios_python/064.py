'''Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

usuario = 0
contador = 0
acumulador = 0

while usuario != 999:
    usuario = int(input('Insira um número (999 para parar): '))
    contador += 1
    acumulador += usuario

acumulador = acumulador - 999
print(f'Você digitou {contador} números e a soma total foi: {acumulador}')