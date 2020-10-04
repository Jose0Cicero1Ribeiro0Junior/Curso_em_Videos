#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

cont = 0

while True:
    pc = randint(0, 10)

    print('=-'*40)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('-='*40)

    n = int(input('Diga um valor: '))
    P_I = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()


    print('-'*40)

    print(f'Você jogou {n} e o computador {pc}. Total de {n+pc} DEU ', end='')
    
    if (n+pc) % 2 == 0:
        print('PAR')
        print('-'*40)
        
        if P_I == 'P':
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            cont += 1
        
        else:
            print('Você PERDEU!')
            break
    else:
        print('ÍMPAR')
        print('-'*40)
        
        if P_I == 'I':
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            cont += 1
        
        else:
            print('Você PERDEU!')
            break

print('GAMER OVER! Você venceu {} vezes'.format(cont))


