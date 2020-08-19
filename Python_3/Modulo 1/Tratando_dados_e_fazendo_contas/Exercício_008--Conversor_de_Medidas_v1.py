#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
medida = float(input('Uma distância em metros: '))
cm = medida *100
mm = medida* 1000
print(f'A media de {medida}m corresponde a {cm}cm e {mm}mm')
