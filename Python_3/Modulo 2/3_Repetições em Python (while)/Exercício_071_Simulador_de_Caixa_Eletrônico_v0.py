#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

saque = int(input('Quanto quer sacar? '))
cont50 = cont20 = cont10 = cont1 =0
while True:
    if 
    if saque // 50:
        saque -= 50
        cont50 += 1
    elif saque // 20:
        saque -= 20
        cont20 += 1
    elif saque // 10:
        saque -= 10
        cont10 += 1
    elif saque // 1:
        saque -= 1
        cont1 += 1
    else:
        break

print('Volte sempre ao BANCO CEV! Tenha um bom dia!')