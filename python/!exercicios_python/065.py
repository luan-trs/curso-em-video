'''Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
 O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

continuar = None
maior = menor = media = contador = 0

while continuar != 'n':
    num = int(input('Digite um número: '))
    contador += 1
    media += num
    
    continuar = input('Quer continuar? (s/n) ').lower()
    if contador == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

media = media/contador
print(f'\nVocê digitou {contador} números e a média foi: {media:.2f}')
print(f'O maior número foi: {maior} e o menor: {menor}')