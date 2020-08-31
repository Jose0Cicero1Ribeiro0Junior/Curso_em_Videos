#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano = int(input('Ano de nacimento: '))
ano_atual = date.today().year
idade = ano_atual - ano
print(f'Sua idade é de {idade}')

if idade < 18:
    print('Faltam {} anos para seu alistamento'.format(idade - 18))
elif idade == 18:
    print('Você já deve se alistar no serviso militar ')
elif idade > 18:
    print('Já se passaram {}anos para seu alistamento'.format(18 - idade))
