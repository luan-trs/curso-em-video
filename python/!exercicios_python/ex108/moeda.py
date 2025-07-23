def metade(valor):
    return valor/2

def dobro(valor):
    return valor*2

def aumentar(valor, porcentagem):
    return valor+(valor/100*porcentagem)

def diminuir(valor, porcentagem):
    return valor-(valor/100*porcentagem)

def moeda(valor, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')