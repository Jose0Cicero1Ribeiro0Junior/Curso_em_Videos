#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = 'Salário do Funcionario que tiveram 15% de aumento este mês'
print(salario.center(30, '='))
while True:
    salario = str(input('Digite o valor do salário: R$'))
    if salario.isnumeric() == True:
        salario = int(salario)
        break
print('O salário do funcionario é de {:.2f} com aumento de 15% fica  {:.2f}'.format(salario, salario + (salario* 15/100)))

#Desafio faça um programa que pegue o produto e pergunte se vai pagar a vista o no cartão se for no cartão vai ser em debito credito se for credito em quantas vezes
#AVISTA DESCONTO
#DEBITO DESCON
#PARCELADO ATÉ 3 PREÇO NORMAL ACIMA DE 3 JUROS CRECENTE
