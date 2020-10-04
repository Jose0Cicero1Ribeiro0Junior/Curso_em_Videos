#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista_num = []
while True:
    num = int(input('Digite um número: '))
    if num not in lista_num:
        lista_num.append(num)
        print('Foi adicionado com sucesso!')
    else:
        print('O número e duplicato não sera adicionado!')
    s_n = ' '
    while s_n not in 'SN':
        s_n = str(input('Quer continuar: [S/N]: ')).strip().upper()
    if s_n == 'N':
        break
print(f'Você digitou os valores {lista_num}')
