#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.


n = str(input('Digite o parametro: ')).strip()
abreto = n.count('(')
fechado = n.count(')')
if abreto == fechado:
    print('Parametro Correto')
else:
    print('Parametro Incorreto')