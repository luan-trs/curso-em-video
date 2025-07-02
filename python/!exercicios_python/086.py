'''Criar uma matriz 3x3 e preencher com valores lidos pelo teclado. 
Ao final, mostrar a matriz como uma tabela 3x3'''
matriz = []
linha = []
for i in range(3):
    for j in range(3):
        linha.append(int(input(f'Número na posição ({i}, {j}): ')))
    matriz.append(linha[:])
    linha.clear()

print('\nMatriz 3x3 organizada:')
for i in range(3):
    print(f'\033[33m{matriz[i]}')
print('\033[0m')