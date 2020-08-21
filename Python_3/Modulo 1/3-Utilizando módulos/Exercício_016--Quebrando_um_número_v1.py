#Crie um programa que leia em número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
import math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))
