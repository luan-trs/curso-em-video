'''Soma dos números ímpares que são
múltiplos de 3 de 1 a 500'''
soma = 0
for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        soma += i
    else:
        pass
print(soma)

# solução otimizada:
'''for i in range(3, 496, 6)
        print(i)'''
# essa resolução foi extraída dos comentários do video da resolução