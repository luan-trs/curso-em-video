# Escreva um programa que leia a quantidade de kilometros percorridos por um carro
# alugado e quantos dias foram usados (dia = R$60 e km = R$15)
dias = int(input('Durante quantos dias o carro foi usado? '))
km = float(input('Qual a quantidade de quilômetros rodados? '))
preço_km = km * 0.15
preço_dias = dias * 60
print ('O total a pagar é:\nR${:.2f}'.format(preço_km + preço_dias))