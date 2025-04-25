# Aumento do salário
salario = float(input('Digite o salário do funcionário: '))
menor = (salario/100)*15
maior = (salario/100)*10
if salario <= 1250.0:
    print(f'O salário ficará com o valor de: R${salario+menor}')
else:
    print(f'O salário ficará com o valor de: R${salario+maior}')