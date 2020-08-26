#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cidade = str(input('Nome da cidade: ')).strip().title()
n = cidade.count('Santo')
if n > 0:
    print('Essa cidade tem o nome Santo ')
    