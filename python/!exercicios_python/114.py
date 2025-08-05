'''Crie um código em python que teste se o site Pudim está acessível pelo computador usado.'''
import http.client
host = "pudim.com.br"
try:
    conn = http.client.HTTPSConnection(host)
    conn.request("GET", "/")
except:
    print('\033[31mO site Pudim não está acessível no momento.\033[0m')
else:
    print('\033[32mConsegui acessar o site Pudim com sucesso!\033[0m')

#O Guanabara fez utilizando a urllib, porém utilizei o módulo http