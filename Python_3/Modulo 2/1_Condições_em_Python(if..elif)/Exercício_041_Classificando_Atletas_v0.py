#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

#– Até 9 anos: MIRIM

#– Até 14 anos: INFANTIL

#– Até 19 anos: JÚNIOR

#– Até 25 anos: SÊNIOR

#– Acima de 25 anos: MASTER

from datetime import date

atual = date.today().year
ano = int(input('Ano de nacimento: '))
idade = atual - ano

print(f'Sua idade é de {idade}, você está na categoria de ', end='')

if idade < 9:
    print('MIRIM')
if idade >= 9 and idade < 14:
    print('INFANTIL')
if idade >= 14 and idade < 19:
    print('JÚNIOR')
if idade >= 19 and idade < 25:
    print('SÊNIOR')
if idade >= 25:
    print('MASTER')
