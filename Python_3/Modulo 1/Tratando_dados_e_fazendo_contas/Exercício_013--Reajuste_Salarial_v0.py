#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = 'Salário do Funcionario que tiveram 15% de aumento este mês'
print(salario.center(30, '='))
while True:
    salario = str(input('Digite o valor do salário: R$'))
    if salario.isnumeric() == True:
        salario = int(salario)
        break
print('O salário do funcionario é de {:.2f} com aumento de 15% fica  {:.2f}'.format(salario, salario + (salario* 15/100)))