#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

galera = list()
nome_peso = list()
pesadas = list()
leves = list()

while True:
    nome_peso.append(str(input('Nome: ')))
    nome_peso.append(float(input('Peso: ')))

    galera.append(nome_peso[:])
    nome_peso.clear()

    s_n = ' '
    while s_n not in 'NS':
        s_n = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if s_n == 'N':
        break
cont = 0
cont_leve = 0
print(f'Foi cadastrado {len(galera)} pessoas.')
for x, y in enumerate(galera):
    if galera[x][1] >= 60.0:
        pesadas.append(y)
        cont += 1
    else:
        leves.append(y)
        cont_leve += 1
for z in range(0, cont):
    print(f'As pessoas mais pesadas são {pesadas[z][0]}', end='... ')
print()
for q in range(0, cont_leve):
    print(f'As pessoas mais leves são {leves[q][0]}', end='... ')
