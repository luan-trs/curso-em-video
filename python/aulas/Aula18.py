pessoas = []
dado = []
maiores = menores = 0
for c in range(3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    pessoas.append(dado[:])
    dado.clear()

for p in pessoas:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        maiores += 1
    else:
        print(f'{p[0]} é menor de idade')
        menores += 1

print(f'Total de maiores de idade: {maiores}\nTotal de menores de idade: {menores}')