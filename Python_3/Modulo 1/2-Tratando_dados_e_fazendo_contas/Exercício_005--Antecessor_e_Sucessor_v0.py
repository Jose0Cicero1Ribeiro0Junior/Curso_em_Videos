#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
while True:
    numero = str(input('Digite um número: '))
    if True == numero.isnumeric():
        numero = int(numero)
        break
    else:
        print('Não é um número tente novamente!')
        print()
print()
print(f'O número que foi digitado {numero} o seu sucessor {numero+1} e o seu antecessor {numero-1}.')
