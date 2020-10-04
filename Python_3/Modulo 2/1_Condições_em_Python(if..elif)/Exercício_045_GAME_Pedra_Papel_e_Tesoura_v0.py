#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
joken = ['pedra', 'papel', 'tesoura']

pc = randint(0,2)
print('[1] - pedra\n[2] - papel\n[3] - tesoura')

jogador = int(input('Qual você escolhe? '))

print('JOKEN')
sleep(1)
print('PO')
sleep(0.5)
print(f'O pc jogou {joken[pc]} e o Jogador jogou {joken[jogador-1]}')
if pc == 0:
    if jogador == 1:
        print('Empate') 
    elif jogador == 2:
        print('Jogador GANHOL!!!')
    elif jogador == 3:
        print('PC GANHOL!!!')
elif pc == 1:
    if jogador == 1:
        print('PC GANHOL!!!') 
    elif jogador == 2:
        print('Empate')
    elif jogador == 3:
        print('Jogador GANHOL!!!')
elif pc == 2:
    if jogador == 1:
        print('Jogador GANHOL!!!') 
    elif jogador == 2:
        print('PC GANHOL!!!')
    elif jogador == 3:
        print('Empate')
