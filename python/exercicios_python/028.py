#jogo da adivinhação (numeros)
import random
user = int(input('Digite um número de 0 a 5: '))
choice = random.randint(0, 5)

if user > 5:
    print('Digite um número válido!')
    exit()

print ('-----------------')
print (f'Eu escolho {choice}')
print ('-----------------')
if choice == user:
    print ('Computador venceu!')
else:
    print('Você venceu!')
print ('-----------------')