#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista_n = list()
for c in  range(1, 6):
    n = int(input(f'Digite o {c}°: '))
    if c == 1 or  n > lista_n[-1]:
        lista_n.append(n)
        print('Número adicionado no final da lista!')
    else:
        pos = 0
        while pos <= len(lista_n):
            if n <= lista_n[pos]:
                lista_n.insert(pos,n)
                print(f'Adicionado na posição {pos+1} da lista...')
                break
            pos += 1

print('-='*30)
print(f'O valores digitados em ordem são: {lista_n} ')


