'''Refazer o exercicio 35
classificar em equilatero, isoceles ou escaleno'''
reta1 = float(input('Qual o valor da primeira reta? '))
reta2 = float(input('Qual o valor da segunda reta? '))
reta3 = float(input('Qual o valor da terceira reta? '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('É possível formar um triângulo')
    if reta1 == reta2 and reta3:
        print('Este triângulo é EQUILÁTERO')
    elif reta1 == reta2 or reta3 == reta1 or reta3 == reta2:
        print('Este triângulo é ISÓCELES')
    elif reta1 != reta2 and reta3:
        print('Este triângulo é ESCALENO')
else:
    print('Não é possível formar um triângulo')
