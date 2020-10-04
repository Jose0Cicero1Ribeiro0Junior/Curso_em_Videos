#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

pc_pensa = str(randint(0,10))
cont = 0

while True:

    usuario = str(input('Qual número o pc está pensadon de 0 à 10 ? '))



    if pc_pensa == usuario:
        pc_pensa = int(pc_pensa)
        usuario = int(usuario)
        print('Você acertou!!')
        break

    else:
        pc_pensa = int(pc_pensa)
        usuario = int(usuario)
        print('Você Errou!!!!')
        print('Tente novamente !!!')
        cont+=1
        
        if pc_pensa > usuario:
            print('Número maior')
        
        elif pc_pensa < usuario:
            print('Numero menor')
        
        elif pc_pensa == usuario:
            print('Você acertou!!')
            break

print(f'Você escolheu {usuario}, e eu escolhi o número {pc_pensa}, Você palpito {cont + 1} até acertar.')
