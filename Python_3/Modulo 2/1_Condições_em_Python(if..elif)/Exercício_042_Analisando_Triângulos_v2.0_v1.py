#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

#– EQUILÁTERO: todos os lados iguais

#– ISÓSCELES: dois lados iguais, um diferente

#– ESCALENO: todos os lados diferentes

print('-='*20)
print('Analizandor de Triângulos')
print('-='*20)

r1 = float(input('Primeiro valor: '))
r2 = float(input('Sengundo valor: '))
r3 = float(input('Terceiro valor: '))

if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('Os segmentos acima PODEM FORMA triângulo')
    if r1 == r2 and r2 == r3:
        print('EQUILÁTERO')
    elif r1!=r2!=r3!=r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMA triângulo')
    