'''Sub do atleta
9 = mirim
14 = infantil
19 = junior
25 = senior
+25 = master'''

import datetime

ano = datetime.datetime.today().year
nascimento = int(input('Em que ano você nasceu? '))
idade = ano - nascimento
print(f'Você tem ou irá fazer {idade} anos')
if idade > 25:
    print('Sua categoria é: \033[1;32mMASTER')
elif idade <= 25:
    print('Sua categoria é: \033[1;32mSÊNIOR')
elif idade <= 19:
    print('Sua categoria é: \033[1;32mJÚNIOR')
elif idade <= 14:
    print('Sua categoria é: \033[1;32mINFANTIL')
elif idade <= 9:
    print('Sua categoria é: \033[1;32mMIRIM')