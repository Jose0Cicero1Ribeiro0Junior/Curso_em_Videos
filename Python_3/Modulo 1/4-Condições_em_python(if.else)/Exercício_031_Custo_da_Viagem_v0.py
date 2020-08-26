#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
viagem = int(input('Qual a distancia da viagem? Km '))
if viagem <= 200:
    preço = viagem * 0.50
if viagem > 200:
    preço = viagem * 0.45
print('O preço da sua passagem é de R${:.2f}'.format(preço))
