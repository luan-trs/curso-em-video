'''Faça um mini sistema que utilize o interactive help do python. O usuário vai digitar o comando e o manual
vai aparecer. Quando o usuário digitar "FIM", o programa se encerrará. OBS: use cores '''
from time import sleep

def ajuda(cmd):
    titulo(f'Acessando o manual do comando \'{comando}\'', 'azul')
    sleep(0.3)
    print('\033[47m')
    help(cmd)
    print('\033[0m')

def titulo(msg, cor):
    cores = {
        'vermelho':'\033[41m',
        'verde':'\033[42m',
        'amarelo':'\033[43m',
        'azul':'\033[44m',
        'magenta':'\033[45m',
        'ciano':'\033[46m',
        'branco':'\033[47m',
    }
    tamanho = len(msg)+4
    print(cores[cor])
    print('~'*tamanho)
    print(msg.center(tamanho))
    print('~'*tamanho)
    print('\033[0m')

while True:
    titulo('SISTEMA DE AJUDA PyHELP', 'verde')
    comando = str(input('Função ou biblioteca > '))
    if comando.lower() == 'fim':
        break
    ajuda(comando)
titulo('ATÉ LOGO!', 'vermelho')