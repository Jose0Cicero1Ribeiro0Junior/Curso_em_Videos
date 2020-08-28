#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('-='*20)
print('Analizandor de Triângulos')
print('-='*20)

r1 = float(input('Primeiro valor: '))
r2 = float(input('Sengundo valor: '))
r3 = float(input('Terceiro valor: '))

if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('Os segmentos acima PODEM FORMA triângulo')
else:
    print('Os segmentos acima NÃO PODEM FORMA triângulo')
    