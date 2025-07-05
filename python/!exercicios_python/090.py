'''Ler o nome e média de um aluno. Também deverá guardar a situação do aluno (media >= 7 será aprovado).
No final, mostre o conteudo da estrutura na tela'''
aluno = dict(Nome = str(input('Nome do aluno: ')), 
             Média = float(input('Média do Aluno: ')))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')