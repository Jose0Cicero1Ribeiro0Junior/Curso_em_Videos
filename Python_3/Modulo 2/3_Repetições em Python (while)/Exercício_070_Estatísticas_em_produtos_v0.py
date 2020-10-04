#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

#A) qual é o total gasto na compra.

#B) quantos produtos custam mais de R$1000.

#C) qual é o nome do produto mais barato.

cont_MAIOR_PREÇO = menor_preço = total = cont = 0
nome_menor_preço = ' '

while True:
    nome = str(input('Nome do produto: ')).strip().title()
    preço = float(input('Preço do produto: R$'))
    total += preço
    cont += 1
    if cont == 1:
        menor_preço = preço
        nome_menor_preço = nome
    if preço < menor_preço:
        menor_preço = preço
        nome_menor_preço = nome
    if preço >= 1000:
        cont_MAIOR_PREÇO += 1


    s_n = ' '
    while s_n not in 'SN':
        s_n = str(input('Quer continuar? [S/N] ')).strip().upper()
    if s_n == 'N':
        break

print(f'O total da compra foi de {total}')
print(f'A quantidade de produtos comprados com o valor maior que R$ 1000,00 são de {cont_MAIOR_PREÇO}')
print(f'O nome do produto com o menor preço é {nome_menor_preço}')
