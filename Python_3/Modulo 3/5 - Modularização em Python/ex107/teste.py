#Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

import Moeda

p = float(input('Digite o preço: R$'))
print(Moeda.aumento(p, 3))
print(Moeda.diminuir(p, 3))
print(Moeda.dobro(p))
print(Moeda.metade(p))
