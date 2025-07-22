'''Função fatorial() que recebe 2 parâmetros: numero a calcular e show, que será um valor lógico opcional
indicando se é mostrado ou não na tela o calculo fatorial'''
def fatorial(numero, show=False):
    """
    ---> Calcula o fatorial de um número:
    :param numero: o número a ser calculado.
    :param show: (opcional) mostra o cálculo sendo realizado.
    :return: o valor fatorial do número calculado.
    """
    f = 1
    for c in range(numero, 0, -1):
        f *= c
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')
    return f

help(fatorial)
print(fatorial(5, show=True))