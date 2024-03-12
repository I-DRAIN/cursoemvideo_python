""" Crie um codigo em Python que teste se o site Pudim esta acessivel pelo computador usado."""

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[0;31mO site Pudim nao esta acessivel no momento\033[033m')
else:
    print('Consegui acessar o site com sucesso!')
    