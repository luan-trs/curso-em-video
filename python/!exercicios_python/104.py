'''Função leiaInt() que funciona de forma semelhante ao input() só que aceitando apenas valores numéricos'''
def leiaInt(mensagem):
    while True:
        num = str(input(mensagem))
        if num.isnumeric():
            num = int(num)
            return num
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[0m')

n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')