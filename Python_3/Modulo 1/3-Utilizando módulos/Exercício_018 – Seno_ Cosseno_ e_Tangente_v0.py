#Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import cos, sin, tan, radians
num = float(input('Digite o ângulo que deseja: '))
num = radians(num)
seno = sin(num)
cosseno = cos(num)
tangente = tan(num)
print(f'O ângulo de {num} tem o :\nSENO {seno:.2f}\nCOSSENO {cosseno:.2f}\nTANGENTE {tangente:.2f}')
