'''Comparar dois numeros inteiros e mostrar as seguintes msgs:
o primeiro numero é maior
o segundo numero é maior
os dois sao iguais'''
num = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num > num2:
    print('O primeiro número é maior')
elif num2 > num:
    print('O segundo número é maior')
else:
    print('Os dois são iguais')