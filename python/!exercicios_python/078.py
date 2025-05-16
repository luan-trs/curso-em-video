'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas posições na lista'''
nums = []
for n in range(5):
    nums.append(int(input(f'Digite um valor para a posição {n}: ')))

maior = nums[0]
menor = nums[0]