#Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import randint
lista_de_alunos = ['José Cicero Ribeiro Junior', 'Fabricia Ramos de Amorim', 'Jose cicero ribeiro','Lurdes','Adriana','Diana','Bruno','Davi']
sorteado = randint(0,len(lista_de_alunos)-1)
print(sorteado)
print('O aluno sorteado foi {}'.format(lista_de_alunos[sorteado]))
