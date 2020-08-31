#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

#– Média abaixo de 5.0: REPROVADO

#– Média entre 5.0 e 6.9: RECUPERAÇÃO

#– Média 7.0 ou superior: APROVADO

lista = []
media = 0
num = int(input('Quantas notas o aluno tem? '))

for c in range(0,num):
    nota = float(input(f'Digite a {c+1}° nota: '))
    lista.insert(c,nota)

for c in range(0,len(lista)):
    media+= lista[c]
    if c+1 == len(lista):
        media/=len(lista)

print(f'Sua média foi de {media:.2f}, você foi ', end='')

if media < 5.0:
    print('REPROVADO')
if media >= 5.0 and media <= 6.9:
    print('para a RECUPERAÇÃO')
if media >= 7:
    print('APROVADO')
 