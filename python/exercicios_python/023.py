# Crie um código que leia um número de 0 a 9999 e mostre cada dígito separado
# Nesse exercício eu não sabia nem como começar, tive q ver a resolução
num = int(input('Digite um número até 9999: '))
print(f'Analisando o número {num}')
unidade = num % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print(f'A unidade deste número é: {unidade}')
print(f'A dezena deste número é: {dezena}')
print(f'A centena deste número é: {centena}')
print(f'O milhar deste número é: {milhar}')
