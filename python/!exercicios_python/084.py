'''Ler o nome e peso de várias pessoas, guardando em uma lista e no final mostre:
A) quantas pessoas foram cadastradas
B) listagem das pessoas mais pesadas
C) listagem das pessoas mais leves'''
pessoas = []
dados = []

while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:]) #Guarda o array atual no array de pessoas, depois o limpa
    dados.clear()

    continuar = str(input('Deseja continuar? [s/n] ')).lower()
    if continuar == 'n':
        break
print(f'A) Total de pessoas cadastradas: {len(pessoas)}')

#Procura o maior e o menor peso e seus nomes na matriz
maior_peso = pessoas[0][1]
menor_peso = pessoas[0][1]
maior_nome = pessoas[0][0]
menor_nome = pessoas[0][0]
for p in range(len(pessoas)):
    if pessoas[p][1] > maior_peso:
        maior_peso = pessoas[p][1]
        maior_nome = pessoas[p][0]
    if pessoas[p][1] < menor_peso:
        menor_peso = pessoas[p][1]
        menor_nome = pessoas[p][0]
print(f'B) O maior peso registrado foi: {maior_peso:.2f}kg, por {maior_nome}')

print(f'C) O menor peso registrado foi: {menor_peso:.2f}kg, por {menor_nome}')