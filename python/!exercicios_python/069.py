#Ler a idade e sexo de várias pessoas e a cada entrada perguntar se o usuario deseja continuar
#No final mostre: quantas pessoas têm mais de 18 anos, 
#quantos homens foram cadastrados e quantas mulheres têm menos de 20 anos
maior18 = homens = mulheres20 = 0


while True:
    print('-=-'*15)
    print('CADASTRE UMA PESSOA')
    print('-=-'*15)
    idade = int(input('Idade: '))
    sexo = input('Sexo: [m/f] ')
    
    if idade >= 18:
        maior18 += 1
    if sexo == 'm':
        homens += 1
    if idade >= 20 and sexo == 'f':
        mulheres20 += 1
    
    print('---'*15)
    continuar = input('Quer continuar? [s/n] ').lower()
    if continuar == 'n':
        break
print(f'Pessoas maiores de 18 anos: {maior18}')
print(f'Homens: {homens}')
print(f'Mulheres maiores de 20 anos: {mulheres20}')
