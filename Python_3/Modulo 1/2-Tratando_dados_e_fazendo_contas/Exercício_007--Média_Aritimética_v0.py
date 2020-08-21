#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
notas = []
c = 0 
while True:
    numero = str(input(f'{c+1}° número: '))
    print(c)
    if True == numero.isnumeric():
        notas.append(int(numero))
        c+=1
    elif False == numero.isalnum():
        c-=1    
    if c == 2:
        break
print(f'A primeira nota {notas[0]} a segunda nota {notas[1]} a média ', end='')
if ((notas[0] + notas[1]) / 2 ) % 1 == 0:
    print(f'{(notas[0] + notas[1]) / 2:.0f}')
else:
    print(f'{(notas[0] + notas[1]) / 2:.2f}')
    