'''Jokenpo'''
import random
jokenpo = ['Pedra', 'Papel', 'Tesoura']
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
maquina = random.choice(jokenpo)
user = int(input('Digite sua escolha: '))
if maquina == 'Pedra' and user == 2:
    print('Papel amassa pedra, você \033[1;34mVENCEU!')
elif maquina == 'Pedra' and user == 3:
    print('Pedra quenbra tesoura, você \033[1;31mPERDEU!')
elif maquina == 'Papel' and user == 1:
    print('Papel amassa pedra, você \033[1;31mPERDEU!')
elif maquina == 'Papel' and user == 3:
    print('Tesoura corta papel, você \033[1;34mVENCEU!')
elif maquina == 'Tesoura' and user == 1:
    print('Pedra quebra tesoura, você \033[1;34mVENCEU!')
elif maquina == 'Tesoura' and user == 2:
    print('Tesoura corta papel, você \033[1;31mPERDEU!')
else:
    print('\033[1;32mEmpate')
# num = [1, 2, 3]
# for i in zip(num, jokenpo):
#     print(i)
# (1, 'Pedra')
# (2, 'Papel')
# (3, 'Tesoura')