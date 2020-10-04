#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
med_idade = hom_idade = mulher_Menor = 0
nome = ''
for c in range(1, 5):
    nom = str(input('Digite o seu nome: ')).strip().title()
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('M/F: ')).strip().upper()

    med_idade += idade

    if sexo == 'M':
        if idade > hom_idade:
            hom_idade = idade
            nome = nom
            print(hom_idade)
    if sexo == 'F':
        if idade < 20:
            mulher_Menor += 1
med_idade /= 4
print(f' A média de idade do grupo é de {med_idade}')
print(f'O nome do homem mais velho é {nome}')
print(f'O número de mulheres menores do que 20 é de {mulher_Menor}')
