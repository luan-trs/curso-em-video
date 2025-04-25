# Faça um programa que leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro e o último nome separadamente
nome = input('Digite seu nome completo: ').split()
primeiro = nome[0]
ultimo = nome[len(nome)-1]
print ('Prazer em te conhecer!')
print (f'Seu primeiro nome é: {primeiro}, e seu último {ultimo}')
# esse foi dificil slk