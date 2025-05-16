'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
#num.insert(2, 2)
num.remove(2)
print(num)
print(f'Essa lista tem {len(num)} elementos.')'''

'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v} → ', end='')'''

valores = []
for cont in range(1, 5):
    valores.append(int(input('Digite um número: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Acabou')