'''Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto
simples. O sistema vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.'''

from lib.interface import *
from time import sleep

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Programa'])
    match resposta:
        case 1:
            cabeçalho('Ver Pessoas Cadastradas')
        case 2:
            cabeçalho('Cadastrar Nova Pessoa')
        case 3:
            cabeçalho('Saindo do Programa...')
            break
        case _:
            print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
