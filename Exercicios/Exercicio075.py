''' Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
    a) Quantas vezes apareceu o numero 9.
    b) Em que posicao foi digitado o primeiro valor 3.
    c) Quais foram os numeros pares. '''

from random import randint

n1 = randint(0,20)
n2 = randint(0,20)
n3 = randint(0,20)
n4 = randint(0,20)

numeros = (n1,n2,n3,n4)

if 9 in numeros:
    print(f'O numero 9 foi digitado {numeros.count(9)} vez(es)')
else:
    print('O numero 9 nao foi digitado')

if 3 in numeros:
    print(f'O numero 3 foi digitado na posicao {numeros.index(3)}.')
else:
    print('O numero 3 nao foi digitado.')

pares = []
for c in numeros:
    if c%2 == 0:
        pares.append(c)

print(f'Os numeros pares digitados foram {pares}.')
