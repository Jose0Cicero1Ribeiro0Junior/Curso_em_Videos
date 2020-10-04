#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
tot = 0
núm = int(input('Digite um número: '))
for c in range(1, núm + 1):
    if núm % c == 0:
        print('\033[33m', end='')
        tot+= 1
    else:
        print('\033[31m' ,end='')
    print('{} '.format(c), end='')
print('\n\033[m0 número {} foi divisível {} vezes'.format(núm, tot))
if tot == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO!')
