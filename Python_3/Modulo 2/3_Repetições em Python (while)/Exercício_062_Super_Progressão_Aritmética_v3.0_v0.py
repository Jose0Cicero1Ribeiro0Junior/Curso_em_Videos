# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
while True:
    primeiro = int(input('Primeira termo: '))
    razão = int(input('Razão: '))
    décimo = primeiro + (10 - 1) * razão

    c = 0
    if primeiro == 0:
        print('Programa FInalizado')
        break
    elif primeiro > 0:
        while True: 
        #for c in range(primeiro, décimo + razão, razão):
            print('{}'.format(primeiro), end ='-> ')
            primeiro += razão
            c+=1
            if c == 10:
                print('ACABOU')
                break
        print()
        opção = str(input('Gostaria de mostrar mais algum termo? [S/N]')).strip().upper()
        if opção == 'S':
            continue
        elif opção == 'N':
            break
        else:
            print('Devido ao erro imposto pelo usuario, acontecera uma reação aleatoria!!!')
print('ACABOU! Volte sempre')