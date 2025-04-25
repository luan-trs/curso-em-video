#Ler o nome e preço de vários produtos (perguntar se o usuario deseja continuar)
#No final deve mostrar: total gasto, quantos produtos custam mais de R$1000 e o nome do produto mais barato
produto = preco = continuar = nomeBarato = precoBarato = maisDe1k = total = 0

print('-=-'*15)
print('LOJA')
while True:
    print('-=-'*15)
    produto = input('Nome do produto: ')
    preco = float(input('Preço do produto: '))

    if preco >= 1000:
        maisDe1k += 1

    if preco > precoBarato:
        nomeBarato = produto
        precoBarato = preco

    total += preco
    print('---'*15)

    continuar = input('Deseja continuar? [s/n] ').lower()
    if continuar == 'n':
        break
print('---'*7,' FIM ', '---'*7)
print(f'O total da compra foi de: R${total:.2f}')
print(f'{maisDe1k} produtos custam mais de R$1000')
print(f'O produto mais barato foi: {nomeBarato}, custando R${precoBarato:.2f}')