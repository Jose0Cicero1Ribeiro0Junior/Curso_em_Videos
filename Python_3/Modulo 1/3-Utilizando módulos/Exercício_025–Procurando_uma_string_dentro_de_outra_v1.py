#Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = str(input('Qual é seu nome? ')).strip()
print('Seu nome tem Silva? {}'.format('silva'in nome.lower()))
