#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = int(input('Qual é o seu sálario? '))

if salario > 1250:
    aumento =(salario + salario * 10/100)
    porcentagem = 10
else:
    aumento = (salario + salario * 15/100)
    porcentagem = 15

print('O seu salario é de R${:.2f} e agora com o aumento de {:.0f}% passa a ser R${:.2f}'.format(salario, porcentagem, aumento))
