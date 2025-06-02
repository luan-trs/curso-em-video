'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas posições na lista'''
nums = []
maior = indexMaior =  -1
menor = indexMenor = 999

for n in range(5):
    add = int(input(f"Digite um valor para a posição {n}: "))
    nums.append(add)
    if add > maior:
        maior = add
        indexMaior = nums.index(add)
    if add < menor:
        menor = add
        indexMenor = nums.index(add)

print(f"\nO maior número foi: {maior}, na posição {indexMaior}")
print(f"O menor número foi {menor} na posição {indexMenor}")