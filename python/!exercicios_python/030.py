# Par ou ímpar
num = int(input('Digite um número: '))
par = bool(num%2 == 0)
if par == True:
    print('Este número é par!')
else:
    print('Este número é ímpar!')