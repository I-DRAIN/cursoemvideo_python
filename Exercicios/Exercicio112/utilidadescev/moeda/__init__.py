def aumentar(preco = 0, taxa = 0, formato=False):
    res = preco + (preco*taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preco = 0, taxa = 0, formato=False):
    res =  preco - (preco*taxa/100)
    return res if formato is False else moeda(res)


def dobro(preco = 0, formato = False):
    res = preco * 2
    return res if formato is False else moeda(res)


def metade(preco = 0, formato = False):
    res = preco/2
    return res if formato is False else moeda(res)


def moeda(preco = 0, moeda='R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=10, taxar=5):
    print('-'*40)
    print('RESUMO DO VALOR'.center(40))
    print('-'*40)
    print(f'Preco analisado: \t{moeda(preco)}')
    print(f'Dobro do preco: \t{dobro(preco, True)}')
    print(f'Metade do Preco:\t{metade(preco, True)}')
    print(f'Com {taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'Com {taxar}% de reducao: \t{diminuir(preco, taxar, True)}')
    print('-'*40)

