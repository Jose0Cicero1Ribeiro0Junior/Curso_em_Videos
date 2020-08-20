#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi aludado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 pot Km rodado
txt = 'Aluguel de carro'
print(txt.center(40))
while True:
    km = str(input('Quantos km o carro se locomovel: Km'))
    dia = str(input('Quantos dias o carro foi usado: '))
    if km.isnumeric() == dia.isnumeric() == True:
        km = int(km)
        dia = int(dia)
        break
print(f'O custo pelo aluguel do carro foi de R${km * 0.15 + dia *60:.2f}')
