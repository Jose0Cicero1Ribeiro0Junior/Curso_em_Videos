#Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
peso = float(input(f'Qual é o peso da 1°: '))
maior = peso
menor = peso
for c in range(2, 6):
    peso = float(input(f'Qual é o peso da {c}°: '))

    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print(f'O menor peso foi {menor} e o maior peso foi {maior}')
