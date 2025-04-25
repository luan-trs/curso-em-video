#leia o comprimento de três retas e diga se é possível formar um triangulo
reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite o valor da segunda reta: '))
reta3 = float(input('Digite o valor da última reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')

#tive q ver video aula no yt