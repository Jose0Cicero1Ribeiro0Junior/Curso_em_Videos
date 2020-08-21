#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
d = 'Descontão de 5% para qualquer produto '
print(d.center(30, '='))
while True:
    preco = str(input('Digite o valor do produto: R$'))
    if preco.isnumeric() == True:
        preco = int(preco)
        break
print('O valor do produto é de {:.2f} com desconto de 5% fica por {:.2f}'.format(preco, preco - (preco* 5/100)))
