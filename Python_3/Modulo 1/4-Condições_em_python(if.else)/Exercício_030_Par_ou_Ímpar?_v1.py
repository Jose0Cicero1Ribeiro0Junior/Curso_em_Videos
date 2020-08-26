#Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Digite um número qualquer: '))
if num % 2 == 0:
    print('Par')
if num % 2 == 1:
    print('Impar')