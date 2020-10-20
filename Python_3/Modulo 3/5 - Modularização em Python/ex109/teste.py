#Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.


import Moeda

p = float(input('Digite o preço: R$'))
print(Moeda.aumento(p,10))