'''Adapte o código do exercício 107, criando uma função adicional chamada moeda() que consiga mostrar os valores
como um valor monetário formatado'''
import moeda

valor = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(valor=valor, porcentagem=10))}')
print(f'Diminuindo 10%, temos {moeda.moeda(moeda.diminuir(valor=valor, porcentagem=10))}')
