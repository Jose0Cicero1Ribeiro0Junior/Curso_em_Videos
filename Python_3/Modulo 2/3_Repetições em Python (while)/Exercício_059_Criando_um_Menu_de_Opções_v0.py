#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar

#[ 2 ] multiplicar

#[ 3 ] maior

#[ 4 ] novos números

#[ 5 ] sair do programa

#Seu programa deverá realizar a operação solicitada em cada caso.
opção = 0 
while opção != 5:
    n1 = int(input('Primeiro valor: '))
    n2 = int(input('Segundo valor: '))
    print()
    while True:
        print(n1, n2)
        print()
        print('O que desejá fazer com esse número? ')
        print("""
    [ 1 ] somar

    [ 2 ] multiplicar

    [ 3 ] maior

    [ 4 ] novos números

    [ 5 ] sair do programa
        """)
        opção = int(input('Escolha uma dessas opções: '))

        if opção == 1:
            resultado = n1 + n2
            break
        elif opção == 2:
            resultado = n1 * n2
            break
        elif opção == 3:
            resultado = n1
            if resultado < n2:
                resultado = n2
            break
        elif opção == 4:
            print('Voltando')
            break
        elif opção == 5:
            print('Saindo do programa')
            break
    if opção != 4:
        if opção != 5:
            print(f'O resultado foi {resultado}')
print('Fim do programa!!!')
