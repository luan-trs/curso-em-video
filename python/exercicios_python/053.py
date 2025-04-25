'''Detector de palíndromos (ex. subi no onibus)'''
frase = input('Digite uma frase: ').replace(' ', '').lower() 

palindromo = frase[::-1]
if palindromo == frase:
    print('\033[32mEsta frase é um palíndromo!')
else:
    print('Esta frase não é um palíndromo')

'''Não vi necessidade de usar o loop for nesse exercício'''