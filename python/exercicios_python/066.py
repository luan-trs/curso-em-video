#Crie um programa que leia vários números inteiros e para quando 999 é digitado.
#Mostre a soma e quantos números foram digitados (desconsiderando a flag)

num = soma = cont = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Você digitou {cont} números')
print(f'A soma total foi: {soma}')