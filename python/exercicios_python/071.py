#Crie um programa que simule o funcionamento de um caixa eletrônico
#No início, pergunte ao usuário qual será o valor a ser sacado (inteiro)
#o programa dirá quantas cédulas de cada valor serão entregues (Considere notas de: R$50, R$20, R$10 e R$1)
notas50 = notas20 = notas10 = notas1 = 0
print('\033[32m***'*15)
print('CAIXA ELETRÔNICO')
print('***'*15, '\033[0m')

valor = int(input('Quanto deseja sacar? R$'))

while True:
    if valor//50 > 0:
        notas50 = valor//50
        valor = valor-50*notas50
        print(f'Notas de R$50: {notas50} ')
    if valor//20 > 0:
        notas20 = valor//20
        valor = valor-(20*notas20)
        print(f'Notas de R$20: {notas20}')
    if valor//10 > 0:
        notas10 = valor//10
        valor = valor-(10*10)
        print(f'Notas de R$10: {notas10}')
    if valor%10 > 0:
        moedas = valor%10
        valor = valor-moedas
        print(f'Moedas de R$1: {moedas}')
    break
print('\033[32m*** FIM DO PROGRAMA ***\033[0m')