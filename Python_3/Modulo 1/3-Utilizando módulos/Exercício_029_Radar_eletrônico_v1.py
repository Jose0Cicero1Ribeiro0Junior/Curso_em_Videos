#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = int(input('Qual foi a velociade? Km '))
if velocidade > 80:
    print('Você foi multado {}'.format((velocidade - 80) *7))
else:
    print('Você não foi multado.')
    