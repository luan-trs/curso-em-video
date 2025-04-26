'''Enunciado muito grande, vou simplificar
dinheiro = 10% desconto
a vista cartão = 5%
até 2x = preço normal
3x ou mais = 20% de juros'''

from random import randint
preço = randint(100, 10000)
print('='*30, f'\033[1;36m{'LOJAS LUANZIN':^20}\033[0m', '='*30)

print(f'Sua compra deu o total de: \033[1;35mR${preço}\033[0m')
print('\033[1;32m1 - Dinheiro = 10% desconto')
print('2 - À vista no cartão = 5% de desconto')
print('3 - Até 2x = preço normal')
print('4 - 3x ou mais = 20% de juros\033[0m\n')

user = int(input('\033[1;36mDigite a forma de pagamento: \033[0m'))

if user == 1:
    dinheiro = preço - (preço / 100 * 10)
    print(f'O valor ficará em: \033[1;32mR${dinheiro:.2f}\033[0m')
elif user == 2:
    vista = preço - (preço / 100 * 5)
    print(f'O valor ficará em: \033[1;32mR${vista:.2f}\033[0m')
elif user == 3:
    print(f'O valor ficará em: \033[1;32mR${preço:.2f}\033[0m')
elif user == 4:
    parcela = preço + (preço / 100 * 20)
    print(f'O valor ficará em: \033[1;32mR${parcela:.2f}\033[0m')
else:
    print('\033[1;31mOpção inválida\033[0m')