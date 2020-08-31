# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

#– O primeiro valor é maior

#– O segundo valor é maior

#– Não existe valor maior, os dois são iguais

lista = []
for c in range(0,2):
    c+=1
    n = int(input(f'Digite o {c}° valor: '))
    lista.insert(c, n)
for c in range(0, len(lista)):
    print(lista[c], end=' ')
print()
if lista[0] > lista[1]:
    print(f'O primeiro valor é maior')
elif lista[0] < lista[1]:
    print(f'Segundo valor é maior')
elif lista == lista[1]:
    print('Não existe valor maior, os dois são iguais.')
