'''Super progressão aritmética''' #Retorna valores enquanto o usuário não dizer 0

primeiro = int(input('Digite um número: ')) 
razao = int(input('Digite a razão: '))
contador = 1
total = 0
continuar = 10 #Inicia o programa com 10 termos, e depois mostra a quantidade de termos do input

while continuar != 0:
    total += continuar
    while contador <= total:
        print(f'{primeiro} → ', end='')
        primeiro += razao #Faz a PA
        contador += 1 #Determina a duração do programa
    print('Pausa')
    continuar = int(input('\nQuantos números mais deseja mostrar? ')) #Caso o usuário responda 0, o programa se encerrará
print('Fim')

print(f'\033[33mO programa foi finalizado com {total} termos mostrados.\033[0m')