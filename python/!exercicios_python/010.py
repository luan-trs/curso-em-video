#Crie um programa que veja quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela póde comprar
print ('$ Este código leva em consideração que o dólar custe R$3,27! $\n (não coloque vírgula, apenas ponto)')
carteira = float(input('Quanto de dinheiro você deseja transformar em dólar? R$'))
#dólar = 3.27
cambio = carteira / 3.27 #dólar
print ('Com R${} você pode comprar {:.2f} dólares!'.format(carteira, cambio))