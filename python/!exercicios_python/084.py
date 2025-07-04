'''Ler o nome e peso de várias pessoas, guardando em uma lista e no final mostre:
A) quantas pessoas foram cadastradas
B) listagem das pessoas mais pesadas
C) listagem das pessoas mais leves'''
pessoas = []
dados = []

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:]) #Guarda o array atual no array de pessoas, depois o limpa
    dados.clear()

    continuar = str(input('Deseja continuar? [s/n] ')).lower()
    if continuar == 'n':
        break
print('-=-'*15)
print(f'A) Total de pessoas cadastradas: {len(pessoas)}')

print(f'B) O maior peso registrado foi: {maior:.2f}kg, peso de: ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print(f'C) O menor peso registrado foi: {menor:.2f}kg, peso de: ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')