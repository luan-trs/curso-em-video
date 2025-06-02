'''Crie um programa onde o usuário possa digitar vários valores (até dizer "n")
e cadastre-os em uma lista. Caso o número já exista lá dentro, ele NÃO será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
lista = list()
valor = 0

while True:
    valor = input('Valor único a ser adicionado: ')
    
    if valor.lower() == 'n':
        break
    if (int(valor) not in lista):
        lista.append(int(valor))
        print("\033[32mVALOR ADICIONADO COM SUCESSO\033[0m")
    else:
        print("\033[31mVALOR NÃO ADICIONADO\033[0m")

lista.sort()
print(f"\n\033[33mLista em ordem crescente: {lista}")