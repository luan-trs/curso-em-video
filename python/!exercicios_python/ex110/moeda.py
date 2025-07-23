def metade(valor, formatar=False):
    result = valor/2
    return result if formatar is False else moeda(result)

def dobro(valor, formatar=False):
    result = valor*2
    return result if formatar is False else moeda(result)

def aumentar(valor, porcentagem, formatar=False):
    result = valor+(valor/100*porcentagem)
    return result if formatar is False else moeda(result)

def diminuir(valor, porcentagem, formatar=False):
    result = valor-(valor/100*porcentagem)
    return result if formatar is False else moeda(result)

def moeda(valor, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')

def resumo(valor, aumento, reducao):
    print('-'*32)
    print('RESUMO DO VALOR'.center(32))
    print('-'*32)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(valor, aumento, True)}')
    print(f'{reducao}% de redução: \t{diminuir(valor, reducao, True)}')
    print('-'*32)
