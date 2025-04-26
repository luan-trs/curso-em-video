'''Sequencia de Fibonacci com while'''
# Retorna a quantidade de termos da sequencia de Fibonacci que o usuário inserir
# Formula de Fibonacci: Fn = F¹-1 + F²-2, sendo os primeiros termos igual a 1

quantidade = int(input('Quantos termos da sequência? '))
contador = 2 #Como os dois primeiros números são 1, eles já serão automaticamente mostrados.
n1 = 1
n2 = 1

print(f'{n1} → {n2} → ', end='')

while contador <= quantidade:
    fibonacci = n1 + n2
    print(f'{fibonacci} → ', end='')
    n1 = n2
    n2 = fibonacci
    contador += 1
print('Fim')