#Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nom = str(input('Seu nome completo: ')).strip().title()
print(f'O seu nome é {nom}')
nom = nom.split()
print(f'O seu primeiro nome é {nom[0]}')
print('É o seu último nome é {}'.format(nom[len(nom)-1]))
