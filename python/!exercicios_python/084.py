'''Ler o nome e peso de várias pessoas, guardando em uma lista e no final mostre:
A) quantas pessoas foram cadastradas
B) listagem das pessoas mais pesadas
C) listagem das pessoas mais leves'''
pessoas = []
dados = []

while True:
    dados.append(input('Nome: '))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:]) #Guarda o array atual no array de pessoas, depois o limpa
    dados.clear()

    continuar = str(input('Deseja continuar? [s/n] ')).lower()
print(f'Total de pessoas cadastradas: {len(pessoas)}')

print('O maior peso registrado foi: ')

print('O menor peso registrado foi: ')