# Leia uma frase e mostre: Quantas vezes aparece a letra 'A',
# Em que posição ela aparece pela primeira vez e pela ultima vez
frase = input('Digite uma frase: ').upper().replace("Á", "A").strip()
quantas_vezes = frase.count('A')
primeiro = frase.find('A')+1
último = frase.rfind('A')
print (f'A letra A apareceu {quantas_vezes} vezes na frase')
print (f'A primeira letra A apareceu na posição {primeiro}')
print (f'A letra A aparece pela última vez na posição {último}')