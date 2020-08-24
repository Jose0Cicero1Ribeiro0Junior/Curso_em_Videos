#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

#– O nome com todas as letras maiúsculas e minúsculas.

#– Quantas letras ao todo (sem considerar espaços).

#– Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em amiúsculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('O seu primeiro nome é {} e ele tem {} letras'.format(separa[0],len(separa[0])))
