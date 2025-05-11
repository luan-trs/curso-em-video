'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado 
e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3. 
C) Quais foram os números pares.'''

nums = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f"Você digitou os seguintes valores: {nums}")

a = nums.count(9)
print(f"\nO número 9 apareceu {a} vezes")

if 3 in nums:
       b = nums.index(3)
       print(f"O número 3 apareceu primeiramente na {b+1}ª posição")
else:
     print("O número 3 não foi digitado")

print(f"Os números pares foram: ", end=' ')
for n in nums:
    if (n%2 == 0):
        print(n, end='')

'''c = []
for n in nums:
    if (n%2 == 0):
        c.append(n) #Caso o número seja par, ele será adicionado à lista
print(f"Os números pares foram: {c}")''' #Primeira maneira que fiz