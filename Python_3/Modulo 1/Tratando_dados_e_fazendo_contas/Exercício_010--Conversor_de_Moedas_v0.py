#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
n = ' Conversor de dolar em real '
print(n.center(40, '='))
while True:
    n = str(input('Quanto você tem na carteira? '))
    if n.isnumeric() == True:
        n = int(n)
        break
print(f'Você tem ${n/5.63:.2f}')
#Desafio fazer disso um conversor de moedas!!!!!!!!!!!!!!!!!