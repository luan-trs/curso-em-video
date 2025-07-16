'''Função chamada escreva() que recebe um texto como parâmetro e mostra uma mensagem com tamanho adaptável
(As linhas de cima e debaixo devem ter o mesmo tamanho da mensagem)'''
def escreva(texto):
    tamanho = len(texto)+4
    print('~'*tamanho)
    print(f'  {texto}')
    print('~'*tamanho)

escreva('Título')