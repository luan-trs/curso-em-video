'''Melhore o desafio 28
o computador pensará em um número entre 0 e 10
o jogador deverá tentar adivinhar até acertar'''
from random import randint

palpites = 0
num = randint(0, 10)

print('-=-'*15)
print(('\033[33mTente acertar o número entre 0 e 10!\033[0m'))
acertou = False

while acertou != True:
    user = int(input('Sua escolha: '))
    palpites += 1
    if user == num:
        acertou = True #encerra o loop
    else: 
        if user < num:
            print('\033[31mMais...Tente novamente!\033[0m')
        if user > num:
            print('\033[31mMenos...Tente novamente!\033[0m')
    


print(f'\033[32mVocê acertou em {palpites} tentativas. Parabéns!\033[0m')
