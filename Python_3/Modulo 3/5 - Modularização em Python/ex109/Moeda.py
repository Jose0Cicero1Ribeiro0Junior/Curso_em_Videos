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
