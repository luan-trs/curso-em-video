try:
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    c = a/b
except Exception as erro:
    print(f'Tivemos um problema. {erro.__class__}')
else:
    print(f'O resultado é {c:.2f}')
finally:
    print('Volte sempre!')