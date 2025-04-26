# Sorteie a ordem das apresentações da turma 
# Ele nem explicou listas ainda
import random
n1 = input('Qual o nome do primeiro aluno? ')
n2 = input('Qual o nome do segundo aluno? ')
n3 = input('Qual o nome do terceiro aluno? ')
n4 = input('Qual o nome do quarto aluno? ')
n5 = input('Qual o nome do quinto aluno? ')
alunos = [n1, n2, n3, n4, n5]
ordem = random.shuffle(alunos)
print ('A ordem sorteada foi:')
print (alunos)