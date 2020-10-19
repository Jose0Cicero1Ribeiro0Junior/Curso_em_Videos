import Moeda

p = float(input('Digite o preço: R$'))
print(Moeda.moeda(Moeda.aumento(p, 3)))
print(Moeda.moeda(Moeda.diminuir(p,3)))
print(Moeda.moeda(Moeda.dobro(p)))
print(Moeda.moeda(Moeda.metade(p)))
