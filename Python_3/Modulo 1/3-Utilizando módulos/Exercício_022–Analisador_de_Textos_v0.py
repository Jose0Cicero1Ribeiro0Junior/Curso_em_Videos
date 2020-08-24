#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

#– O nome com todas as letras maiúsculas e minúsculas.

#– Quantas letras ao todo (sem considerar espaços).

#– Quantas letras tem o primeiro nome.
while True:
    nom = str(input('Digite seu noume copleto: ')).title().split()
    nom = " ".join(nom)
    print('\nO seu nome {}'.format(nom))
    s_n = str(input('Confere ? (S/N) ')).upper().strip()
    if s_n == 'S':
        break
print('O seu nome com todas as letras minusculas: {}\nO seu nome com todas as letras maiusculas: {}'.format(nom.lower(),nom.upper()))
nom1 = "".join(nom.split())
print('O seu nome tem ao todo sem considerar os espaços:  {} letras'.format(len(nom1)))
nom2 = nom.split()
print(f'O seu primeiro nome tem {len(nom2[0])} letras')
