#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a área e a quantidade de tinta necessária para pinta-lá, sabendo que cada litro de tinta pinta uma área de 2m².
nom = 'Calculo de Pintura de parede'
print(nom.center(40,'='))
while True:
    b = str(input('Qual é a largura da parde: '))
    h = str(input('Qual é a altura da parede: '))
    if b.isnumeric() == h.isnumeric() == True:
        b = int(b)
        h = int(h)
        break
A = b*h
litro_tinta = A/2
print(f'A área de sua parede é de {A}, você tera que gastar {litro_tinta}L de tinta para poder pintar a parede.')
