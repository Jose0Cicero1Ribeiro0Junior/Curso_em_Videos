#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto

#– à vista no cartão: 5% de desconto

#– em até 2x no cartão: preço formal 

#– 3x ou mais no cartão: 20% de juros

produto = float(input('Valor do produto: R$'))
print('Como deseja pagar?\n1 - A vista no dinheiro ou cheque\n2 - A vista no cartão\n3 - Em até 2x no cartão sem juros\n4 - 3x ou mais no cartão')
n = int(input(''))

print(f'O preço do produto é de R${produto}', end='')

if n == 1:
    produto = produto - (produto * 10/100)
    print(f' com o desconto de 10% o produto fica de R${produto}')
elif n == 2:
    produto = produto - (produto * 5/100)
    print(f' com o desconto de 5% o produta fica de R${produto}')
elif n == 3:
    produto = produto / 2
    print(f' dividido no cartão em 2x o produto fica de R${produto} em 2x')
elif n == 4:
    print()
    n = int(input('Em quantas vezes desejá dividir o valor? '))
    if n >= 3:
        n-=2
        produto = produto + (n * produto * 20/100)
        n+=2
        dividido = produto / n
    print(f'.O preço a ser pago é de R${produto} dividido em {n}x fica em R${dividido:.2f}')
