#desenvolva um programa que some as notas de um aluno e faça uma média
nota1 = int(input( 'Primeira nota: '))
nota2 = int(input('Segunda nota: '))
nota3 = int(input('Terceira nota: '))
media = (nota1+nota2+nota3) / 3
print ('A média do aluno é:{:,.2f}'.format(media))