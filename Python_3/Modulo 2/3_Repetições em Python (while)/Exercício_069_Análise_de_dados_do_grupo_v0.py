#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

#A) quantas pessoas tem mais de 18 anos.

#B) quantos homens foram cadastrados.

#C) quantas mulheres tem menos de 20 anos.

cont = contM = contF = 0 
while True:
    id = int(input('Quatos anos: '))
    sexo = str(input('Qual é o sexo: [M/F]: ')).strip().upper()

    if id > 18:
        cont += 1

    if sexo == 'M':
        contM += 1

    if sexo == 'F':
        if id >= 20:
            contF += 1

    s_n = str(input('Quer continuar [S/N]: ')).strip().upper()
    
    if s_n == 'N':
        break
print(f'\nA quantidade de pessoas cadastradas maiores de 18 são de {cont}\nA quantidade de homens cadastrados é de {contM}\nA quatidade de mulheres cadastrada maiores de 20 anos é de {contF}')
