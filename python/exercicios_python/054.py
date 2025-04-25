'''Ler o nome de 7 pessoas e dizer quantas tem mais de 18 e quantas não'''
cont = 0
for i in range(1, 8):
    pessoa = int(input('Digite a idade das pessoas: '))
    if pessoa >= 18:
        cont += 1
print('\nDentre essas pessoas: ')
print(f'\033[32m{cont} pessoas já atingiram a maioriadade')
print(f'{7 - cont} pessoas não atingiram a maioriade')