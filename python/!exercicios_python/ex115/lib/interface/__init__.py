def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[0m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[0m')
            return 0
        else:
            return num

def linha(tamanho=42):
    return '-' * tamanho

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    for n, item in enumerate(lista):
        print(f'\033[33m{n+1}\033[0m - \033[34m{item}\033[0m')
    print(linha())
    opc = leiaInt('\033[32mSua escolha: \033[0m')
    return opc
