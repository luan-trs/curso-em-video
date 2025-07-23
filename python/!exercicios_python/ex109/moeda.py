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