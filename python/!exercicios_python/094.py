'''Ler o nome, sexo e idade de várias pessoas e guardar os dados de cada um em um dicionário e todos os
dicionários em uma lista. No final mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade do Grupo
C) Uma lista com todas as mulheres
D) Uma lista com todas as pessoas com idade acima da média'''
pessoas = []
pessoa = {}
media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True: 
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'FM':
            break
        print('\033[41mERRO!\033[0m Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    media += pessoa['idade']
    pessoas.append(pessoa.copy())

    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if continuar in 'SN':
            break
        print('\033[41mERRO!\033[0m Responda apenas S ou N.')
    if continuar == 'N':
        break

print('-=-'*20)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')

media = media/len(pessoas)
print(f'B) A média de idade é de {media:.2f} anos')

print(f'C) As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'\033[42m{p["nome"]}\033[0m / ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média:')
for p in pessoas:
    if p['idade'] > media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('\n\033[41m<< ENCERRADO >>\033[0m')