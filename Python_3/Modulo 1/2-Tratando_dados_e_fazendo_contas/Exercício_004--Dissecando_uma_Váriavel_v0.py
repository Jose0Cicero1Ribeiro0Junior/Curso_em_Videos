#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ela.
n = str(input('Digite: '))
print()
is_is = [n.isalnum(),n.isalpha(),n.isascii(),n.isdecimal(),n.isdigit(),n.isidentifier(),n.islower(),n.isnumeric(),n.isprintable(),n.isspace(),n.istitle(),n.isupper()]
is_is_name = ['alfanuméricos','alfabéticos','pode ser impressa','consiste apenas em dígitos','identificador válido em Python','minúsculas','numéricos','imprimíveis ou vazia','apenas caracteres de espaço','string com capa de título','maiúsculas']
for c in range(0, len(is_is)-1):
    print(n,'=>', is_is_name[c],'=>', end=' ')
    if is_is[c] == True:
        print('\033[0;31;36m Verdadeiro \033[m')
    else:
        print('\033[0;31;31m Falso \033[m')
    print()
    