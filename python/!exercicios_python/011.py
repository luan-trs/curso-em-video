#Crie um programa que leia a largura e altura de uma parede e calcule sua área e quantidade de tinta necessária
print ('Cada litro de tinta pinta 2m²')
b = int(input('Qual ao tamanho da base de sua parede? '))
h = int(input('Qual a altura de sua parede? '))
a = b*h
tinta = a/2
print ('Você irá precisar de {} litros de tinta.'.format(tinta))
