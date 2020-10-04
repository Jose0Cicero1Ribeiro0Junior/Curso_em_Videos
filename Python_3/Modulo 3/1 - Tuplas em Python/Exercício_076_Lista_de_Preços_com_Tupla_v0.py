# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

preço = ('Manteiga200g' , 2.00 , 'Queijo 1kg' ,25.00)
cont = 0
print({:^50}.format('LISTAGEM DE PREÇO'))
print('_'*50)
print()
for x in range(0,len(preço)):
    if cont % 2 == 1:
        print(preço[x])
    elif cont % 2 == 0:
        print(preço[x], end=' R$')
    cont +=1
print('_'*50)
print()