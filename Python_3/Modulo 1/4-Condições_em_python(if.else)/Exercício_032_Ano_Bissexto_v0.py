#Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
bissexto = int(input('Qual ano que você deseja saber se é bissexto? '))
bissexto = bissexto / 4 % 1
print(bissexto)
if bissexto == 0:
    print('Esse ano é bissexto.')
else:
    print('Esse ano não é bissexto.')
    