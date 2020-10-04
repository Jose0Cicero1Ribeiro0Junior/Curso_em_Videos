# Exercício Python 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

números = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte' 

while True:
    n = int(input('Qual número quer por extenso [0 á 20]: '))
    if n >= 0 and n <= 20:
        print(números[n])
        s_n = ' '
        while s_n not in 'SN':
            s_n = str(input('Quer continuar [S/N]: ')).strip().upper()
        if s_n == 'N':
            break

    else:
        print('Tente novamente!')
print('Fim do programa! Volte sempre.')
