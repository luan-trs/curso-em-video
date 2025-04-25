#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo user
#O programa será interrompido quando o valor digitado foi negativo
num = 0
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-=-'*10)
    if num < 0:
        break
    for i in range(1, 11):
        print(f'{num} x {i} = {num*i}')
    print('-=-'*10)
print('\033[31mPROGRAMA ENCERRADO\033[0m')