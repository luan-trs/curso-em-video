#Radar eletrônico
carro = float(input('Qual a velocidade do carro? '))
multa = (carro-80) * 7
if carro > 80:
    print('Você foi Multado!')
    print('Valor da multa: R${:.2f}'.format(multa))

#Tive a mesma linha de raciocinio que o guanabara