'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas posições na lista'''
nums = []
maior = 0
menor = 0

for n in range(5):
    nums.append(int(input(f"Digite um valor para a posição {n}: ")))
    if n == 0:
        maior = menor = nums[n]
    else:
        if nums[n] > maior:
            maior = nums[n]
        if nums[n] < menor:
            menor = nums[n]
print('-=-'*15)
print(f'Você digitou os valores {nums}')

#Verifica as posições do maior e menor número e mostra todos os index
print(f"\nO maior valor foi: {maior}, nas posições ", end='')
for i, v in enumerate(nums):
    if v == maior:
        print(f'{i}... ', end='')
print()

print(f"\nO menor valor foi: {menor}, nas posições ", end='')
for i, v in enumerate(nums):
    if v == menor:
        print(f'{i}... ', end='')
print()
