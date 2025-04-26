# Programa que leia o nome de uma cidade e verifique se ela COMEÇA
# com o nome 'Santo'
# depois da explicação do 22 fiz esse tranquilo
cidade = input('Digite o nome de uma cidade: ').upper().strip()
nome_da_cidade = cidade.split()
verificar = 'SANTO' in nome_da_cidade[0]
print(f'Essa cidade começa com Santo? {verificar}')