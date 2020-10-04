#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

n = int(input('Digite um número: '))
maior = menor = n
cont = soma = media = 0
while True:
    
    s_n = str(input('Quer continuar? [S/N] ')).strip().upper()  
        
    if s_n == 'N':
        cont += 1
        soma += n
        media = soma / cont
        if maior < n:
            maior = n
        if menor > n:
            menor = n
        break

    elif s_n == 'S':
        cont += 1
        soma += n
        media = soma / cont
        if maior < n:
            maior = n
        if menor > n:
            menor = n
        n = int(input('Digite um número: '))

print(f'Você digitou {cont} números e a média foi {media:.2f}\nO maior valor foi {maior} e o menor foi {menor}')
