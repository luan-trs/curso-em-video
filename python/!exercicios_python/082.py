'''Crie um programa que leia vários números e coloque-os em uma lista.
Depois disso, crie  duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. No final mostre o conteúdo das três listas geradas.'''
listaTotal = []
listaPar = []
listaImpar = []

while True:
    num = int(input("Insira um valor: "))
    listaTotal.append(num)
    
    user = input("Deseja continuar? [s/n] ").lower()
    if user == 'n':
        break

for n in listaTotal:
    if n%2 == 0:
        listaPar.append(n)
    else:
        listaImpar.append(n)
        
print(f"\nNúmeros digitados: {listaTotal}")
print(f"Números pares: {listaPar}")
print(f"Números ímpares: {listaImpar}")