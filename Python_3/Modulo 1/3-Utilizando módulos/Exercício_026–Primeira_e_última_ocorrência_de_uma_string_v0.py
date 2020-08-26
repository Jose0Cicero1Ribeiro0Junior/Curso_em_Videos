#Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
fras = str(input('Digite uma frase qualquer: ')).strip().capitalize()
n = fras.lower().count('a')
find = fras.find('a')+1
finr = fras.rfind('a')+1
print(f'Nessa frase a letra "a" aparece {n}\nO "a" aparece pela primaeira vez é na posição {find}\nA ultima posição da letra "a" é {finr}')

