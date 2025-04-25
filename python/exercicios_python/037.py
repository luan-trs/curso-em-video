'''Escreva um programa que leia um número inteiro e peça para o usuário
escolher qual será a base numérica da conversão
1 = binário
2 = octal
3 = hexadecimal'''

print('-=- Conversor de bases decimais -=-')
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
user = int(input('Digite o número da ação: '))
num = int(input('O número que deseja converter: '))

if user == 1:
    print('{} convertido em Binário é: {}'.format(num, bin(num).replace('0b', '')))
elif user == 2:
    print('{} em Octal é: {}'.format(num, oct(num).replace('0o', '')))
elif user == 3:
    print('{} em Hexadecimal é: {}'.format(num, hex(num).replace('0x', '')))