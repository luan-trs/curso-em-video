'''Alistamento do exército, leia o ano de nascimento e diga
se ele ainda vai se alistar, se é hora de se alistar ou se
já passou do tempo'''
import datetime
idade = int(input('Em que ano você nasceu? '))
ano = datetime.datetime.today().year
tempo = ano - idade

if tempo == 18 or 19:
    print('É hora de se alistar!')
elif tempo == 17:
    print('Está chegando a hora!')
elif tempo < 17:
    print('Ainda não é hora de se alistar')
elif tempo > 19:
    print('Já passou da hora de se alistar!')