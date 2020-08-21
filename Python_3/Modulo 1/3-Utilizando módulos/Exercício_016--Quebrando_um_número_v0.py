#Crie um programa que leia em número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
def is_number(num):
    try:
        float(num)
        return True
    except:
        pass
    return False
while True:
    n = str(input('Digite um número Real qualquer: '))
    if is_number(n) == True:
        n = float(n)
        break
print(f'O valor digitado foi {n} e sua porção inteira é {n:.0f}')
