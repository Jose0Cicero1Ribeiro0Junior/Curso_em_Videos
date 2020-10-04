#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.          

print('TABUADA')
print()
n = int(input('Escolha o número que desejá, Ver sua Tabuada : '))

for c in range(0,11):
    print(f"{c:2} x {n:2} = {c*n:2} ")
 