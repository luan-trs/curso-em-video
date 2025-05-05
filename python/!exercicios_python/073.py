times = ('Flamengo', 'Palmeiras', 'Fluminense', 'Ceará', 'Cruzeiro', 'Bragantino', 'Vasco', 'Juventude', 'Mirassol', 'Internacional', 'Botafogo', 'Fortaleza', 'Santos', 'Corinthians', 'Vitória', 'São Paulo', 'Grêmio', 'Bahia', 'Atlético Mineiro', 'Sport')

print('----'*15)
print('Os 5 primeiros colocados foram:')
print(times[:5])

print('----'*15)
print('Os últimos 4 colocados foram:')
ultimos = times[-1], times[-2], times[-3], times[-4], times[-5]
print(ultimos)
print('----'*15)

print('Em ordem altabética: ')
print(sorted(times))
print('----'*15)

if 'Chapecoense' not in times:
  print('A Chapecoense não se encontra na série A')
else:
  chapeco = times.index('Chapecoense')
  print(f'A Chapecoense está na posição {chapeco+1} na tabela')