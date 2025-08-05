def leiaDinheiro(msg):
    while True:
        p = str(input(msg)).replace(',', '.').strip()
        if p.isalpha() or p == '':
            print(f'\033[31mERRO: \"{p}\" é um preço inválido.\033[0m')
        else:
            return float(p)