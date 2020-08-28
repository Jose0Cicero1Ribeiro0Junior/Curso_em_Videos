#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
lista = []
maior = menor = 0
for c in range(0,3):
    n1 = int(input(f'Digite o {c+1}° número: '))
    lista.insert(c, n1)
maior = lista[0]
menor = lista[0]
if maior > lista[1]:
    maior = lista[1]
if maior > lista[2]:
    maior = lista[2]
if menor < lista[1]:
    menor = lista[1]
if menor < lista[2]:
    menor = lista[2]
 
print('O maior numero é {}\nO menor número {}'.format(maior,menor))
