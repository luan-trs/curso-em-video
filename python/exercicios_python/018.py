# Faça um programa que leia um angulo e mostre o valor do seno, cosseno e tangente
# não faço idéia de como fazer pprt
import math
angulo = float(input("Digite um ângulo qualquer: "))
cosseno = math.cos(math.radians(angulo))
seno = math.sin(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print ('Cosseno: {}\nSeno: {}\nTangente: {}'.format(cosseno, seno, tangente))