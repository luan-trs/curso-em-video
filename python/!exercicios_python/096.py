'''Uma função chamada area() que recebe as dimensões de um terreno retangular e mostre a area do terreno'''
print('  Cálculo de área  ')
print('--'*15)

def area(comprimento, largura):
    result = comprimento*largura
    print(f'A área de um terreno {comprimento}x{largura} é de {result:.2f}m²')

area(comprimento=float(input('Comprimento (m): ')), largura=float(input('Largura (m): ')))