#Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

frase = str(input('Digite uma frase: ')).strip()

if frase.lower() == frase[::-1].lower():
    print(f'A frase {frase} é um palíndromo')
else:
    print('Não é um palindromo')