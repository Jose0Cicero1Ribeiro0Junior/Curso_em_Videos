#Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

#– IMC abaixo de 18,5: Abaixo do Peso

#– Entre 18,5 e 25: Peso Ideal

#– 25 até 30: Sobrepeso

#– 30 até 40: Obesidade

#– Acima de 40: Obesidade Mórbida

import math
print('Calculo do IMC')
print()
altura = float(input('Sua altura: (m) '))
peso = float(input('Seu peso: (Km) '))
IMC = peso / altura**2 #divide-se o peso do paciente pela sua altura elevada ao quadrado
print(f'O seu IMC é de {IMC:.2f}')

if IMC < 18.5:
    print('Abaixo do Peso')
elif IMC > 18.5 and IMC < 25:
    print('Peso Ideal')
elif IMC >25 and IMC < 30:
    print('Sobrepeso')
elif IMC > 20 and IMC < 40:
    print('Obesidade')
elif IMC > 40:
    print('Obesidade Morbida')

