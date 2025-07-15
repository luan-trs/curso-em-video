'''Ler o nome, ano de nascimento (mas guardar como idade) e carteira de trabalho e cadastre-os
em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de 
contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar
*Considerando 35 anos de contribuição para se aposentar* '''
from datetime import date
info = {}

info['Nome'] = str(input('Nome: '))

#Lê o ano de nascimento e guarda a idade
ano_nascimento = int(input('Ano de nascimento: '))
info['Idade'] = date.today().year - ano_nascimento

info['CTPS'] = str(input('Carteira de trabalho (0 caso não tenha): '))
if info['CTPS'] != '0':
    info['Ano de contratação'] = int(input('Ano de contratação: '))
    info['Salário'] = float(input('Salário: R$'))
    info['Aposentadoria'] = info['Ano de contratação'] - (date.today().year - info['Idade']) + 35
print('-=-'*20)
for k, v in info.items():
    print(f'  - {k} tem o valor {v}')