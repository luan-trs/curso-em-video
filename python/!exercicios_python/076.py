produtos = (
    'Lápis', 1.75,
    'Bolacha', 3.99,
    'Achocolatado', 7,
    'Borracha', 1,
    'Caderno', 5,
    'Maçã', 0.5,
    'Chocolate', 2.50,
    'Leite', 2,
    'Morango', 8)

print('='*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('='*40)
for item in range(0, len(produtos)):
    if item%2 == 0:
        print(f'{produtos[item]:.<30}', end='') #Mostra os itens de número par (nome do produto) alinhados à esquerda com pontos separando do preço
    else:
        print(f'R${produtos[item]:>7.2f}') #Preço à direita
print('='*40)