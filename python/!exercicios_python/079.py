'''Crie um programa onde o usuário possa digitar vários valores (até dizer "n")
e cadastre-os em uma lista. Caso o número já exista lá dentro, ele NÃO será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
lista = list()
valor = 0

while True:
    valor = int(input('Valor único a ser adicionado: '))
    if valor not in lista:
        lista.append(int(valor))
        print("\033[32mVALOR ADICIONADO COM SUCESSO\033[0m")
    else:
        print("\033[31mVALOR NÃO ADICIONADO\033[0m")

    pergunta = input('Deseja continuar? [s/n] ').lower()
    if pergunta == 'n':
        break

lista.sort()
print(f"\n\033[33mLista em ordem crescente: {lista}\033[0m")