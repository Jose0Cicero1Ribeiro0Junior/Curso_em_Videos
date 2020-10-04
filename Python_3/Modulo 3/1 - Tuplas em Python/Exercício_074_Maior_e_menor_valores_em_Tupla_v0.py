#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

while True:
    n1 = randint(0,1000)
    n2 = randint(0,1000)
    n3 = randint(0,1000)
    n4 = randint(0,1000)
    n5 = randint(0,1000)

    tupla = (n1,n2,n3,n4,n5)
    maior = menor = 0
    print()
    print('O número gerado aleatoriamente foi ', end='')
    for x in range(0,len(tupla)):
        print(tupla[x], end=' -> ')
        if x == 0 or maior < tupla[x]:
            maior = tupla[x]
        if x == 0 or menor > tupla[x]:
            menor = tupla[x]
        
    print('Fim')

    print(f'O menor número é {menor}\nO maior número é {maior}')

    s_n = ' '
    while s_n not in 'SN':
        s_n = str(input('Quer continuar [S/N]: ')).strip().upper()
    if s_n =='N':
        break



