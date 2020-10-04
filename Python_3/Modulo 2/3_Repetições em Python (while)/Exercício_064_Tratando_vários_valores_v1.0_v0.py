#Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
cont = total = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    print()

    if n == 999:
        break
    else:
        total += n
        cont += 1

print(f'\nVocê digitou {cont} número e a soma entre eles foi {total}. ')
