#Conversor universal de binário, decimal, hexadecimal, octal
from time import sleep
opcao = [0,1, 2, 3, 4]
print('Coversor')
print('1 - Binário\n2 - Decimal\n3 - Hexadecimal\n4 - Octal\n')
while True:
    n = str(input('Didite o número de uma das opções acima em que você tem o valor: '))
    if True == n.isnumeric():
        n = int(n)
        if n > 4:
            continue
        elif opcao.index(n):
            print(n, opcao)
            break
    else:
        continue
sleep(1)
if n == 1:
    print('A opção que vc escolheu foi binário, gostaria de convertelo para qual base númerica? ')
    print('1 - Decimal\n2 - Hexadecimal\n3 - Octal\n')
    n = str(input('Didite o número de uma das opções acima em que você tem o valor: '))
