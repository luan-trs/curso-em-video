'''Peça que o usuario informe seu sexo e caso responda
algo diferente de M ou F, peça que responda de novo '''
sexo = input('\033[0mQual seu sexo?\033[31m(M/\033[34mF)\033[0m ').upper().strip()

while sexo not in 'FM' or sexo == '':
    print('\033[31mInválido! Tente novamente')
    sexo = input('\033[0mQual seu sexo?\033[31m(M/\033[34mF)\033[0m ').upper()


resultado = 'masculino' if sexo == 'M' else 'feminino'
print(f'\033[32mVálido! Seu sexo é: \033[0m{resultado}')