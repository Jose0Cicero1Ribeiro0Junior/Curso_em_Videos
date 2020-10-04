#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro = int(input('Primeira termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão

c = 0
while True: 
#for c in range(primeiro, décimo + razão, razão):
    print('{}'.format(primeiro), end ='-> ')
    primeiro += razão
    c+=1
    if c == 10:
        break
print('ACABOU')
