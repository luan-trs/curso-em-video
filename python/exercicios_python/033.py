# Ler 3 números e dizer qual o maior e qual o menor
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))

if num3 > num1 and num2:
    print(f'O número {num3} é o maior número')
elif num2 > num1 and num3:
    print(f'O número {num2} é o maior o número')
elif num1 > num2 and num3:
    print(f'O número {num1} é o maior número')

if num3 < num1 and num2:
    print(f'O menor número é o número {num3}')
elif num2 < num1 and num3:
    print(f'O menor número é o número {num2}')
elif num1 < num2 and num3:
    print(f'O menor número é o número {num1}')
