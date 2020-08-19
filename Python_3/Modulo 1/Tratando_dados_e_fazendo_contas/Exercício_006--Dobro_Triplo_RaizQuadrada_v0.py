#Crie um algoritimo que leia um número e mostre o seu dobro, triplo e sua raiz quadrada.
while True:
    numero = str(input('Digite um número: '))
    if True == numero.isnumeric():
        numero = int(numero)
        break
    else:
        print('Erro tente novamente!!!')
        print()
print(f'O número que foi digitado foi {numero} o seu dobro {numero*2} o seu triplo {numero*3} e o sua raiz quadrada ', end='')
if numero**(1/2) % 1 == 0:
    print(f'{numero**(1/2):.0f}')
else:
    print(f'{numero**(1/2):.2f}')
