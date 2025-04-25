# Calcular passagem
distancia = int(input('Qual a distância da viagem? '))
ate_200km = 0.50
mais_de_200km = 0.45

if distancia >= 200:
    print ('O valor ficará em: R${:.2f}'.format(distancia*mais_de_200km))
else:
    print('O valor ficará em: R${:.2f}'.format(distancia*ate_200km))