#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

while True:
    sexo = str(input('Qual é o seu sexo? [M/F]: ')).strip().upper()
    if sexo in 'MF':
        if sexo == 'M':
            print('Seu sexo é Masculino')
            break
        elif sexo == 'F':
            print('Seu sexo é Feminino')
            break
        elif sexo == 'FM' or sexo == 'MF':
            print('Tente novamente!!!ERRO!!')
        
    else:
        print('Tente novamente!!!ERRO!!')
