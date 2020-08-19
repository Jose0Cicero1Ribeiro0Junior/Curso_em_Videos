#Crie um programa que leia dois números e mostre a soma entre elas.
c = 0
soma =[]
while True :
    n1 = str(input(f'Número {c +1}° : '))
    c+=1
    if False == n1.isnumeric():
        c-=1
    elif True == n1.isnumeric():
        soma.append(int(n1))
    if c == 2:
        break
print(f'A soma entre {soma[0]} + {soma[1]} = {soma[0]+soma[1]}')
