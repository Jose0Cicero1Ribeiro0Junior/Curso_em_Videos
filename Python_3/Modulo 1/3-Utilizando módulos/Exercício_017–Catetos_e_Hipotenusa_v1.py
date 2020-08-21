#Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import hypot
a = float(input('Qual o valor do cateto adjasente: '))
b = float(input('qual o valor do cateto oposto: '))
print('A hipotenusa é: {}'.format(hypot(a, b)))