#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista_n = []
lista_par = []
lista_ímp = list()

while True:
    n = int(input('Digite um número: '))
    lista_n.append(n)

    if n % 2 == 0:
        lista_par.append(n)
    elif n % 2 == 1:
        lista_ímp.append(n)
    s_n = ' '
    while s_n not in 'SN':
        s_n = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if s_n == 'N':
        break
print(f'A lista ao todo é {lista_n}\nA lista só com os número pares é {lista_par}\nA lista de ímpares é {lista_ímp}')
