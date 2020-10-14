#Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def msg(msg):
    tam = len(msg) +4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

print('Escreva : ',end='')
msg(str(input('')).title())