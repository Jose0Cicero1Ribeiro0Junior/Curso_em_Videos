#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
n = []
for x in range(1,6):
    n0 = int(input('Digite um valor um valor na posição {} '.format(x)))
    n.append(n0)

print('-='*50)
print(f'Você digitou os valores {n}')
print(f'O maior valor digitado foi {max(n)} nas posições ', end='')
for i, v in enumerate(n):
    if v == max(n):
        print(f'{i}...', end=' ')
print()
print(f'O menor valor digitado foi {min(n)} nas posições ', end='')
for i, v in enumerate(n):
    if v == min(n):
        print(f'{i}...', end=' ')
print()

