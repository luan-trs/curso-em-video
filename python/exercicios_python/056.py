'''nome idade e sexo de 4 pessoas
mostrar a media de idade
nome do homem mais velho
quantas mulheres tem menos de 20'''

media = 0 # Acumulador que junta as idades e utilizado para fazer a média
mulheres = 0 # Conta quantas mulheres menores de 20 existem
maior = 0 # Maior idade
mais_velho = 0 # Nome do mais velho
homens = 0 # Saber se há homens

for i in range(1, 5):
    nome = input(f'\033[33mQual o nome da {i}ª pessoa?\033[0m ')
    idade = int(input('\033[35mQual a idade dessa pessoa?\033[0m '))
    media += idade # Acumula as idades
    sexo = input('\033[32mQual o sexto da pessoa?(\033[34mm/\033[31mf)\033[0m  ') #m/f
    if sexo in 'Mm':
        homens += 1
    if homens == 1:
        maior = idade
        mais_velho = nome
    elif sexo in 'Mm' and idade > maior:
        maior = idade
        mais_velho = nome
    if idade < 20 and sexo == 'f':
        mulheres += 1
    

print(f'\n\033[33mA média das idades é de: {media/4:.1f} anos')
print(f'O homem mais velho é: {mais_velho} com {maior} anos de idade')
print(f'{mulheres} mulheres têm menos de 20 anos')


'''Consegui resolver sem ver o vídeo!!!!!! (achei dificil)'''