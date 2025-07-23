'''Função notas() que pode receber várias notas de alunos e retorna um dicionário com as seguintes informações:
Quantidade de notas, a maior nota, a menor nota, a média da turma, a situação (opcional).
Adicione também as docstrings da função.'''
def notas(*notas, sit=False):
    """
    ---> Função para analisar notas e situação de vários alunos.\n
    :param notas: recebe um número ilimitado de notas.
    :param sit: (opcional) mostra a situação da sala.
    :return: dicionário com estatísticas sobre a turma.
    """
    dicio = {
        'quantidade':len(notas),
        'maior_nota':max(notas),
        'menor_nota':min(notas),
        'média':sum(notas)/len(notas)    
    }
    if sit:
        if dicio['média'] >= 7:
            dicio['situação'] = 'BOA'
        elif dicio['média'] >= 5:
            dicio['situação'] = 'RAZOÁVEL'
        else:
            dicio['situação'] = 'RUIM'
    return dicio

print(notas(5, 2, 10, 4, sit=True))
help(notas)