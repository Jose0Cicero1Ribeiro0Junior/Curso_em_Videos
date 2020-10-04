# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8


print()
termos = int(input('Quantos termos quer mostrar? '))
n = [0, 1]
c = 0
print()
while len(n) > c < termos:
    print(n[c], end=' - ')
    x = n[c+1] + n[c]
    c += 1
    n.insert(c+1, x)
    
print('FIM')
print()
