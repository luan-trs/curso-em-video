'''Modifique as funções criadas no exercício 107 para que elas aceitem um parâmetro a mais, informando se o valor
retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no exercício 108'''
import moeda

valor = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, formatar=True)}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, formatar=True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(valor=valor, porcentagem=10, formatar=True)}')
print(f'Diminuindo 10%, temos {moeda.diminuir(valor=valor, porcentagem=10, formatar=True)}')
