'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados
na ordem correta.'''
parenteses = [] #Lista onde avaliarei a posição dos parenteses
parentesesAbertos = parentesesFechados = 0
erros = 0

expressao = input("Digite uma expressão numérica: ")
for c in range(len(expressao)):
    if expressao[c] in "(":
        parenteses.append(expressao[c])
        parentesesAbertos+=1
    elif expressao[c] in ")":
        parenteses.append(expressao[c])
        parentesesFechados+=1
        if parentesesAbertos > parentesesFechados or parentesesAbertos < parentesesFechados:
            erros += 1
    

if erros < 1:
    print("\033[32mNenhum erro encontrado")
else:
    print(f"\033[31m{erros} parentêses estão escritos na ordem incorreta")