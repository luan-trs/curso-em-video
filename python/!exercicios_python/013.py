#Faça um algoritmo que aumente o salário de um funcionário em 15%
salario = int(input('Qual o valor do salário? R$'))
porc = salario/100
aumento = salario + porc*15
print ('O salário com 15% de aumento ficará {}'.format(aumento))