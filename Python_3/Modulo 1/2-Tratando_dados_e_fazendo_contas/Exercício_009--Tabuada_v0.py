#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
from time import sleep
txt = 'TABUADA'
print(txt.center(40, '='))
while True:
    numero = str(input('Digite um número para a tabuada: '))
    if numero.isnumeric() == True:
        numero = int(numero)
        break
    else:
        print('Erro!!!')
for x in range(0, 11):
    print(f'{x:2} X {numero:2} = ', end='')
    if x * numero % 1 == 0:
        print(x*numero)
    else:
        print(f'{x*numero:.1f}')
    sleep(0.51)
    