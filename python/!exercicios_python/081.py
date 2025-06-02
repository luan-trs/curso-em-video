'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados
B) A lista de valores ordenados de forma decrescente
C) Se o valor 5 foi digitado e está ou não na lista'''
lista = []
quant = 0

while True:
    num = int(input("Insira um valor: "))
    lista.append(num)
    quant+=1
    
    user = input("Deseja continuar? [s/n] ").lower()
    if user == 'n':
        break

lista.sort(reverse=True)

print(f"\nA) A quantidade de valores digitados foi de: {quant} valores")
print(f"B) Valores ordenados de forma decrescente: {lista}")
if 5 in lista:
    print("C) O número 5 foi digitado e está na lista.")
else:
    print("C) O número 5 não foi digitado e não está na lista")