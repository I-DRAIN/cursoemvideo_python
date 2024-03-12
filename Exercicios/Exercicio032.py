# Faca um programa que leia um ano e mostre se ele e bissexto.

ano = int(input('Digite um ano: '))

if ano % 4 == 0:
    print('O ano {} e bissexto!'.format(ano))
else:
    print('Esse ano tem 365 dias!')