#Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
lista = []
s = cont = 0 
for c in range(1, 7):
    n = int(input('Digite um número para ser somado: '))
    lista.insert(c, n)
    if n % 2 == 0:
        s+=n
        cont+=1
print(f'A soma dos {cont} número pares é de {s}')
