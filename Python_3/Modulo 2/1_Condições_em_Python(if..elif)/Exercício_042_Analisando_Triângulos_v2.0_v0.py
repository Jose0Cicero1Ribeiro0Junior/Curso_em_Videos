#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

#– EQUILÁTERO: todos os lados iguais

#– ISÓSCELES: dois lados iguais, um diferente

#– ESCALENO: todos os lados diferentes

from time import sleep

lista = []

for c in range(0, 3):
    n = float(input('Qual é o comprimento da {}° reta ? '.format(c+1)))
    lista.insert(c, n)

print(lista)  

print('PROCESSANDO...')
sleep(1)

if lista[0] < lista[1] + lista[2] and lista[1] < lista[0] + lista[2] and lista [2] < lista[0] + lista[1]:

    print('É um triangulo ', end='')

    if lista[0] == lista[1] == lista[2]:
        print('EQUILÁTERO')
    
    elif lista[0] == lista[1] != lista[2] or lista[0] == lista[2] != lista[1] or lista[1] == lista[2] != lista[0]:
        print('ISÓSCELES')
    
    else:
        print('ESCALENO')
else:
    print('Não é um triangulo')
