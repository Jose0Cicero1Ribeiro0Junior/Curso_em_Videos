#Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = str(input('Digite seu nome: ')).strip().title()
n = nome.split().count('Silva')
if n > 0:
    print('O seu nome tem Silva!')
print(f'Seu nome {nome}')
