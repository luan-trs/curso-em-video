# Mostre se o ano é bissexto ou não
ano = int(input('Qual ano deseja saber se é bissexto? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é bissexto.')
else:
    print('Esse ano não é bissexto')
