'''Ler o nome e duas notas de vários alunos e guardar em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita com que o usuário possa mostrar as notas
de cada um individualmente (999 interrompe)'''
boletim = []
aluno = []

while True:
    #index 0: nome, index 1: nota1, index 2: nota2, index 3: média
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    aluno.append((aluno[1]+aluno[2])/2) #média
    
    boletim.append(aluno[:])
    aluno.clear()

    pergunta = str(input('Deseja continuar? [s/n] ')).lower()
    if pergunta == 'n':
        break

print('-=-'*15)
print('Nº  NOME        MÉDIA')
print('--'*15)
for num, al in enumerate(boletim):
    print(f'{num:0}{al[0]:^10}     {al[3]:.2f}')

while True:
    print('--'*15)
    acessar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if acessar == 999:
        print('\033[31mPROGRAMA ENCERRADO')
        break
    else:
        print(f'As notas de {boletim[acessar][0]} são {boletim[acessar][1:3]}')