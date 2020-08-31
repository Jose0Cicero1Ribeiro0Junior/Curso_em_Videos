#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

from time import sleep

print('Conversor de base númerica')
num = int(input('Digite um número para ser convertido: '))

sleep(0.5)

print('1 - Binário\n2 - Octal\n3 - Hexadecimal')
base = int(input('Digite uma base de converção '))

print('Convertendo....')

sleep(2)

if base == 1:
    print('O número convertido para binario foi {} > '.format(num), end='')
    num = bin(num)
    print(f' {num[2:]}')

if base == 2:
    print('O número convertido para Octal foi {} > '.format(num),end='')
    num = oct(num)
    print(f'{num[2:]}')

if base == 3:
    print('O número convertido para Hexadecimal foi {} > '.format(num), end='')
    num = hex(num)
    print(f'{num[2:]}')

print('FIM do programa')
