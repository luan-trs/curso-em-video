'''Calcular IMC
abaixo de 18.5 = Abaixo do peso
até 25 = peso ideal
até 30 = sobrepeso
até 40 = obesidade
acima de 40 = obesidade mórbida'''
altura = float(input('Qual sua altura? '))
peso = float(input('Qual o seu peso? '))
imc = peso/(altura**2)
print('Seu imc é: {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal!')
elif imc <= 30:
    print('Você está acima do peso')
elif imc <= 40:
    print('Você está obeso!')
elif imc > 40:
    print('Você possui obesidade mórbida')