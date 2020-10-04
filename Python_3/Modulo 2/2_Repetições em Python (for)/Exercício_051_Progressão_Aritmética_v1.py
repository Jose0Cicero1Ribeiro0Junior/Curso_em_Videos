#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input('Primeira termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
print(décimo)

for c in range(primeiro, décimo + razão, razão):
    print('{}'.format(c), end ='-> ')

print('ACABOU')