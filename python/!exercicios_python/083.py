'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados
na ordem correta.'''

expressao = input("Digite uma expressão numérica: ")
pilha = [] #Armazena os parenteses errados

for c in expressao:
    #Caso o caractere seja um parenteses aberto, ele é adicionado a pilha
    if c == '(':
        pilha.append(c)
    #Caso o parenteses feche, o par é removido da pilha e nao representam um erro
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(c) #Erro identificado
            break
    

if len(pilha) == 0:
    print("\033[32mNenhum erro encontrado.\033[0m")
else:
    print(f"\033[31mSua expressão está errada!\033[0m")