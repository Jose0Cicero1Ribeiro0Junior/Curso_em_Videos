#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resp = 'S'
soma = quant = média = maior = menor = 0

while resp in 'Ss':
    núm = int(input('Digite um número '))
    soma += núm
    quant += 1
    
    if quant == 1:
        maior = menor = núm
    
    else:
        if núm > maior:
            maior = núm

        if núm < menor:
            menor = núm

    resp = str(input('Quer continuar? [S/N ')).upper().strip()[0]

media = soma / quant

print('Você digitou {} número e a média foi {:.2f}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
