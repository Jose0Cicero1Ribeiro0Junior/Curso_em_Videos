#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.

#B) Em que posição foi digitado o primeiro valor 3.

#C) Quais foram os números pares.
cont9 = cont3 = cont_pares = 0
for x in range(0, 4):
    n = int(input(f'\n{x+1}° número: '))
    
    if x == 0:
        n1 = n
    elif x == 1:
        n2 = n
    elif x == 2:
        n3 = n
    elif x == 3:
        n4 = n
    if n == 9:
        cont9 += 1
    elif n == 3:
        cont3 += 1
    if n % 2 == 0:
        cont_pares += 1
n0 = n1, n2, n3, n4

print('\nOs números escolhidos foram: ',n0)

if cont9 > 0:
    print(f'O número 9 aparacesse {cont9}')
if cont3 > 0:
    y = n0.index(3)+1
    print(f'A pososição do primeiro valor número 3 é {y}')
if cont_pares > 0:
    x = 0
    print('Os números pares são : ', end='')
    for x in range(0, len(n0)):
        if n0[x] % 2 == 0:
            print(n0[x], end=',')

print()
