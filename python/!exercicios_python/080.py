'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição de inserção correta (sem usar o sort()).
No final, mostre a lista ordenada na tela.'''
lista = []

for n in range (5):
    num = int(input("Digite um valor: "))
    if n == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista')
    else:
        posicao = 0
        while posicao < len(lista):
            if num <= lista[posicao]:
                lista.insert(posicao, num)
                print('Adicionado na posição ', posicao)
                break
            posicao += 1
print('-=-'*15)
print(lista)