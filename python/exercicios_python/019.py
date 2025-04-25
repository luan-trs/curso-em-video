# um professor quer sortear um de seus 4 alunos, faça um programa que o ajude
# ele nem explicou listas ainda
import random
n1 = input('Qual o nome do primeiro aluno? ')
n2 = input('Qual o nome do segundo aluno? ')
n3 = input('Qual o nome do terceiro aluno? ')
n4 = input('Por fim, qual o nome do quarto aluno? ')
alunos = [n1, n2, n3, n4]
sorteio = random.choice(alunos)
print ('O aluno sorteado foi: {}'.format(sorteio))