'''ler o peso de 5 pessoas de dizer qual o mais pesado e mais leve'''
maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input(f'Qual o peso da {i}ª pessoa? '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'\n\033[33mO maior peso é: {maior}kg')
print(f'O menor peso é de: {menor}kg')