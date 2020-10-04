#Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.


for cont in range(1, 51):
    print(cont, end=' => ')

print()
print('Números IMPARES: ', end='')
for cont in range(1, 51):

    if cont % 2 == 1:
        print(cont, end=' > ')
print()
print('Números PARES: ', end='')
for cont in range(1, 51):
    if cont % 2 == 0:
        print(cont, end=' > ')
