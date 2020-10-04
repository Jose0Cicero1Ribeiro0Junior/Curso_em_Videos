#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    
    x = int(input('\nQuer ver a tabuada de qual valor? '))
    
    print('-'*40)
    
    if x >= 0:
    
        for y in range(1, 11):
            print(f'{x:2} x {y:2} = {x*y:2}')
    
    else:
    
        print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre! \n')
        print('-'*40)
        break
    
    print('-'*40)
