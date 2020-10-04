#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
date = date.today().year
maior = menor = 0
for c in range(1, 8):
    ano = int(input(f'Data de nacimento da {c}° pessoa.'))
    if date - ano >= 18:
        maior += 1
    elif date - ano <= 17:
        menor += 1
print(f'O número de pessoas que atigiram a maioridade é de {maior}')
print(f'O número de pessoas que não atigiram a maioridade é de {menor}')