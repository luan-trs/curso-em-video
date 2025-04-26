'''Aprovamento de empréstimo
variáveis: valor da casa, salário e quantos anos de prestação
Caso a prestação mensal ultrapasse 30% do salário, o empréstimo será negado. '''

valor_casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual seu salário? '))
anos = int(input('Em quantos anos você irá pagar? '))

meses = anos * 12
preço_parcelas = valor_casa / meses
porcentagem = preço_parcelas / 100 * 30

if porcentagem > salario:
    print('Empréstimo NEGADO')
else:
    print('Empréstimo concedido')
