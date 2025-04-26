'''Pegar 6 numeros inteiros e mostrar a soma apenas dos pares'''
soma = 0
for i in range(0, 6):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        soma += num
    else:
        pass
print(f'\033[;33mA soma dos números pares foi: {soma}\033[0m')