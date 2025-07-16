'''Função maior() que recebe vários parâmetros com valores inteiros.
Seu programa deve analisar todos os valores e dizer qual o maior.'''
from time import sleep

#Solução com buit in (max())
'''def maior(*nums):
    print(f'O maior valor digitado é {max(nums)}')'''

#Solução com loop
def maior(*nums):
    print('-=-'*20)
    if len(nums) > 0:
        maior = nums[0]
        print('Analisando os valores inseridos...')
        for n in nums:
            print(f'{n} ', end='', flush=True)
            sleep(0.5)
            if n > maior:
                maior = n
    else:
        maior = 0
    print(f'Foram informados {len(nums)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

maior(2, 9, 6)
maior(2, 45, 92, 32, 12)
maior(10)
maior()