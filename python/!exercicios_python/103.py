'''Função chamada ficha() que recebe 2 parâmetros opcionais, sendo eles o nome de um jogador e quantos gols ele 
marcou. O programa deverá mostrar a ficha do jogador mesmo que algum dado não tenha sido informado corretamente'''
def ficha(nome="<deconhecido>", gols=0):
    if nome.strip() == '':
        nome = '<desconhecido>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {nome} fez {gols} gols no campeonato.')

nome = str(input('Nome: '))
gols = str(input('Gols: '))
ficha(nome, gols)