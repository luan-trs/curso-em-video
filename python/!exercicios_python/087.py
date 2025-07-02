'''Aprimore o desafio anterior mostrando no final:
A) A soma de todos os valores pares digitados
B) A soma dos valores da terceira coluna
C) O maior valor da segunda linha'''
matriz = []
linha = []
soma_pares = 0
for i in range(3):
    for j in range(3):
        valor = int(input(f'Número na posição ({i}, {j}): '))
        if valor%2 == 0:
            soma_pares += valor
        linha.append(valor)
    matriz.append(linha[:])
    linha.clear()

print('\nMatriz 3x3 organizada:')
for i in range(3):
    print(f'\033[33m{matriz[i]}')
print('\033[0m')

print(f'A) Soma dos valores pares da matriz: {soma_pares}')

#Soma os valores da terceira coluna (x, 2)
soma_coluna = matriz[0][2] + matriz[1][2] + matriz [2][2]
print(f'B) Soma dos valores da terceira coluna: {soma_coluna}')

print(f'C) Maior valor da segunda linha: {max(matriz[1])}')