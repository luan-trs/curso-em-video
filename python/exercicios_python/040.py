'''Ler duas notas e fazer média
Abaixo de 5.0 = reprovado
Entre 5.0 e 6.9 = recuperação
7.0 ou mais = aprovado '''
primeira_nota = float(input('Qual foi a primeira nota do aluno? '))
segunda_nota = float(input('Qual foi a segunda nota do aluno? '))
media = (primeira_nota+segunda_nota)/2
print('A média do aluno foi: \033[1;37m{:.2f}'.format(media))

if media >= 7:
    print('O aluno foi \033[1;35mAPROVADO\033[1;37m, PARABÉNS!')
elif media < 5:
    print('O aluno foi \033[1;31mREPROVADO')
elif media > 4.9 and media < 6.9:
    print('O aluno está de \033[1;33mRECUPERAÇÃO')