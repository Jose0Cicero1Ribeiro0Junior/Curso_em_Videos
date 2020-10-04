#Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
print('Contagem Regressiva para o estouro de fogos!!!')

for c in range(1,10):
    print(10 - c)
    sleep(1)
print('BOMMM')
