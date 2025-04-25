# Crie um programa que leia o nome de uma pessoa e mostre se ela tem Silva no nome
nome = input('Digite seu nome completo: ').upper().strip()
sobrenome = 'SILVA' in nome
print(sobrenome)
if sobrenome == True:
    print('Este nome contem Silva.')
else:
    print('Este nome não possui Silva.')

#Eu não deveria usar If e else, mas dei uma enfeitada