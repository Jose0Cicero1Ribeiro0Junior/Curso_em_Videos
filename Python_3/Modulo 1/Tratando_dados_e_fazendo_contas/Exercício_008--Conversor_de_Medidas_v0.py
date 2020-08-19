#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
while True:
    simbolo_metrico = 'km','hm','dam','m','dm','cm','mm'
    metrica = str(input('km,hm,dam,m,dm,cm,mm: ')).lower()
    if metrica in simbolo_metrico:
        break
while True:
    numero = str(input('Digite o tamnho em metros: '))
    if True == numero.isnumeric():
        break
numero = int(numero)
unidade_metrica = ['quilômetro','hectomêtro','decâmetro','metro','decímetro','centímetro','milímetro']
divi = [numero/1, numero/10, numero/100, numero/1000, numero/10000, numero/100000, numero/1000000]
mult = [numero*1000000, numero*100000, numero*10000, numero*1000, numero*100, numero*10, numero*1]
if metrica in 'm':
    print(f'O número em {unidade_metrica[3]} escolhido foi {divi[0]}m.')
    for c in range(0, 3):
        print(f'\nO {unidade_metrica[c]} {mult[c-4]}')
    for c in range(0, 3):
        print(f'\nO {unidade_metrica[c+4]} {divi[c+1]}')
elif metrica in 'km':
    print(f'O número em {unidade_metrica[0]} escolhido foi {divi[0]}km.')
    for c in range(0, 6):
        print(f'\nO {unidade_metrica[c+1]} {divi[c+1]}')
elif metrica in 'hm':
    print(f'O número em {unidade_metrica[1]} escolhido foi {divi[0]}hm.')
    for c in range(0, 1):
        print(f'\nO {unidade_metrica[c]} {mult[c-2]}')
    for c in range(0, 5):
        print(f'\nO {unidade_metrica[c+2]} {divi[c+1]}')
elif metrica in 'dam':
    print(f'O número em {unidade_metrica[2]} escolhido foi {divi[0]}dam.')
    for c in range(0, 2):
        print(f'\nO {unidade_metrica[c]} {mult[c-3]}')
    for c in range(0, 4):
        print(f'\nO {unidade_metrica[c+3]} {divi[c+1]}')
elif metrica in'dm':
    print(f'O número em {unidade_metrica[4]} escolhido foi {divi[0]}dm.')
    for c in range(0, 4):
        print(f'\nO {unidade_metrica[c]} {mult[c-5]}')
    for c in range(0, 2):
        print(f'\nO {unidade_metrica[c+5]} {divi[c+1]}')
elif metrica in 'cm':
    print(f'O número em {unidade_metrica[5]} escolhido foi {divi[0]}cm.')
    for c in range(0, 5):
        print(f'\nO {unidade_metrica[c]} {mult[c-6]}')
    for c in range(0, 1):
        print(f'\nO {unidade_metrica[c+6]} {divi[c+1]}')
elif metrica in 'mm':
    print(f'O número em {unidade_metrica[6]} escolhido foi {divi[0]}mm.')
    for c in range(0, 6):
        print(f'\nO {unidade_metrica[c]} {mult[c-7]}')
