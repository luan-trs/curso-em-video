n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1+n2
su = n1-n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
di = n1 // n2
print ('A soma é {},\n subtração {},\n multiplicação {},\n divisão {:4f},'.format(s, su, m, d), end = ' ' )
print ('a potência é {} e a divisão inteira é {}.'.format(p,di))
# print ('A soma vale {}!'.format(n1+n2))