#Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

total = cont = 0
for soma in range(3 , 501 , 3):
    if soma % 2 == 1:
        cont += 1
        total+=soma
print(f'A soma de todo os {cont} valores solicitados é de {total}')
