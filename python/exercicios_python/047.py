'''Mostrar apenas os números pares de 1 a 50'''
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=' ')
    else:
        pass

# solução otimizada:
'''for i in range(2, 51, 2):
    print(i, end=' ')'''