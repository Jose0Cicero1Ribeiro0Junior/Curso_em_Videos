#Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
numer = 0 
lista = []
while True:
    n1 = str(input('Nome do {}° aluno: '.format(numer+1)))
    numer+=1
    
    if n1 == 'sair':
        break
    else:
        lista.insert(numer,n1)

shuffle(lista)
for c in range(0,len(lista)):
    print(f'{c+1}° - {lista[c]}')
