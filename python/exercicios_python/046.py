'''Contagem regressiva de 10 a 0 com estouro de fogos
pausa de 1 segundo entre elas'''
from time import sleep
import emoji
for i in range(10, 0, -1):
    print(i)
    sleep(1)
print(emoji.emojize(':fireworks: :collision: 0 :collision: :fireworks:'))