# Crie um programa que deixe o nome de alguem maiusculo, minusculo, total de letras(sem espaço)
# e total de letras apenas do primeiro nome
nome = input('Digite seu nome completo: ').strip()
nome_separado = nome.split()
print ('Maiúsculo: {}\nMinúsculo: {}'.format(nome.upper(), nome.lower()))
print(f'Seu primeiro nome é: {nome_separado[0]}\nLetras do primeiro nome:{len(nome_separado[0])}')
print(f'Total de letras (sem espaços): {len(nome.replace(" ", ""))}')
