#Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('http://www.w3.org/1999/xhtml')

except urllib.error.URLError:
    print('O site Pudim não está acessível no momento.')

else:
    print('Consegui acessar o site Pudim com sucesso!')
    print(site.read())
    