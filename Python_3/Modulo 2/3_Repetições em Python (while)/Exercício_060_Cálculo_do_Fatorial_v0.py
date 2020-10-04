#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

#5! = 5 x 4 x 3 x 2 x 1 = 120

n = int(input('Escolha um número para ser fatoriado: ')) 
lista = [n]
c = produto = 1

while n != 0:

    if n != 0:
        lista.insert(c, n)
        n -= 1
        c += 1   

print(f'{c-1}! = ', end= '')

for c in range(1, len(lista)):
    print(lista[c], end='')
    
    if c + 1 < len(lista):
        print( end=' x ')
    produto *= lista[c]

print(end = ' = ')
print('{}'.format(produto))


