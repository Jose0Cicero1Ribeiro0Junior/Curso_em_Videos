#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.Depois disso , mostre:

# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente. 
# C) Se o valor 5 foi digitado e está ou não na lista.

lista_n = []
while True:
    n = int(input('Digite um número: '))
    s_n = ' '
    lista_n.append(n)
    while s_n not in 'SN':
        s_n = str(input('Você quer continuar? [S/N]: ')).strip().upper()
    if s_n == 'N':
        break

print(f'Foi digitado {len(lista_n)}')
lista_n.sort()
lista_n.reverse()
print(f'A ordem decresente é {lista_n}')
if 5 in lista_n:
    print('O valor 5 foi encontrado')
else:
    print('O valor 5 não foi encontrado')
