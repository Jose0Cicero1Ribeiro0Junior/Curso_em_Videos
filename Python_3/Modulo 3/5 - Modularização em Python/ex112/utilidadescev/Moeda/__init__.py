def aumento(preço=0, taxa=0, formato=True):
    res = preço + (preço * taxa/100)
    return res if not formato==True else moeda(res)

def diminuir(preço=0,taxa=0, formato=True):
    res = preço - (preço * taxa/100)
    return res if not formato==True else moeda(res)

def dobro(preço=0, formato=True):
    res = preço * 2
    return res if not formato==True else moeda(res)

def metade(preço=0, formato=True):
    res = preço / 2
    return res if not formato==True else moeda(res)

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:8.2f}'.replace('.',',')

def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisando: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'Com {taxaa}% de aumento: \t{aumento(preço,taxaa)}')
    print(f'Com {taxar}% de redução: \t{diminuir(preço,taxar)}')
    print('-' * 30)
