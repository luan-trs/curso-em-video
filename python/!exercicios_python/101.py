'''Um programa com uma função voto() que recebe o ano de nascimento de uma pessoa, retornando um valor
literal indicando se a pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições'''
from datetime import date

def voto(nascimento):
    print('--'*20)
    idade = date.today().year - nascimento
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO.'
    elif idade < 18 or idade >= 70:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))