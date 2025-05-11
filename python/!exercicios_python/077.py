'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''
palavras = (
    'MERCADO', 'ALMOFADA', 'LINGUIÇA',
    'CHURRASCO', 'POLICIAL', 'COMPUTADOR',
    'GAMEPAD', 'PYTHON', 'SENSEI' 
    )

vogais = ('A', 'E', 'I', 'O', 'U')

for p in palavras:
    print(f'Na palavra {p} temos: ', end='')
    for letra in p:
        if letra in vogais:
            print(f'{letra.lower()}', end=' ')
    print('\n')