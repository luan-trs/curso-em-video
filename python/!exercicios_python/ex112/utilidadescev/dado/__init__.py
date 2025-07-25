def leiaDinheiro(msg):
    while True:
        p = str(input(msg)).replace(',', '.').strip()
        if p.isalpha() or p == '':
            print(f'\033[31mERRO: \"{p}\" é um preço inválido.')
        else:
            return float(p)