'''Progressão aritmética basicamente pegar o primeiro termo e sua razão (seria o início e quantos passos ele vai dar) e mostrar os 10 primeiros números'''
num = int(input('Qual o início da PA? '))
razao = int(input('Qual a razão da PA? '))
decimo = num + (10-1) * razao
for i in range(num, decimo + razao, razao): #num = inicio, 11 pois são 10 numeros e razao = passos
    print(i, end=' → ')
print('Acabou')
