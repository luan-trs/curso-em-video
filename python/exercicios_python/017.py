# Escreva um programa que leia os catetos e retorne a hipotenusa de um tringulo retangulo
import math
cateto1 = float(input('Qual a medida do cateto oposto? '))
cateto2 = float(input('Qual a medida do cateto adjascente? '))
#hipotenusa = cateto1**2 + cateto2**2
#result = sqrt (hipotenusa)
hipotenusa = math.hypot(cateto1, cateto2) 
print ('A hipotenusa deste triângulo é: {}'.format(hipotenusa))