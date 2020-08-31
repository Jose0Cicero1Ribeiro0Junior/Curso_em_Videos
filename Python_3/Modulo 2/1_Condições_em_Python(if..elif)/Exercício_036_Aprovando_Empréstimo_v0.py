#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual é o valor da casa? '))
salario = float(input('Quanto você recebe mensalmente? '))
tempo = int(input('Por quanto tempo pretende pagar? '))

if casa / (tempo*12) > salario * 30/100:
    print('O seu emprestimo bancário foi NEGADO. A prestação mensal que foi de {:.2f} exedel os 30% do seu salário que é de {:.2f} '.format(casa/(tempo*12), salario * 30/100))
else:
    print('O seu emprestimo bancário foi Permitido.')
