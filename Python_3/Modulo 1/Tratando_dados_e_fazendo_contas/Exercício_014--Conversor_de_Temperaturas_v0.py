#Escreva um program que converta uma temperatura digita em °C e converta para  °F
nom = ' Conversor de Temperatura '
print(nom.center(40, '='))
while True:
    c = str(input('Qual é o grau celsius: '))
    if c.isnumeric() == True:
        c = int(c)
        break
print(f'A conversão do grau {c}°C para {c * 9/5 +32}°F ')
#Desafio fazer um converso de temperatura tanto para um quanto para outro = https://www.google.com/search?q=conversor+de+temperatura+f+para+c&oq=conver&aqs=chrome.0.69i59j69i57j35i39j0j69i61j69i65j69i60l2.2005j0j7&sourceid=chrome&ie=UTF-8