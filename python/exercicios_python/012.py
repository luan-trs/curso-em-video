#faça um algoritmo que mostre o preço de um produto com 5% de desconto
produto = int(input('Digite o preço do produto que deseja aplicar um desconto:\n R$'))
porc = (produto/100)*5
desconto = produto - porc
print ('O produto custará {:,.2f} após o desconto ser aplicado.'.format(desconto))