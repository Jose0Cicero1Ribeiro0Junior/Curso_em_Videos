#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
from time import sleep
n = int(input('Digite um valor: '))
print('PROCESSANDO....')
sleep(1)
if n % 2 != 0:
    print('É número primo')  