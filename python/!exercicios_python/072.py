numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

user = int(input('Digite um número entre 0 e 20: '))
while user not in range(len(numeros)):
    user = int(input('Tente novamente. Digite um número de 0 a 20: '))
print(f'Você digitou o número {numeros[user]}')