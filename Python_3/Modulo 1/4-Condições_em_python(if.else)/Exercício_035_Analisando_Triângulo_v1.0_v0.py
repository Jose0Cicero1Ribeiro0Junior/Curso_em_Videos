#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

lista = []
for c in range(0, 3):
    n = float(input('Qual é o comprimento da {}° reta ? '.format(c+1)))
    lista.insert(c, n)

print(lista)    
if lista[0] < lista[1] + lista[2] and lista[1] < lista[0] + lista[2] and lista [2] < lista[0] + lista[1] :
    print('É um triangulo')

else:
    print('Não é um triangulo')
