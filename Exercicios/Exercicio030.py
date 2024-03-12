# Crie um programa que leia um numero inteiro qualquer e mostre na tela se ele e par ou impar.

num = int(input('Digite um numero qualquer: '))

if num % 2 == 1:
    print('O numero {} e impar!'.format(num))
else:
    print('O numero {} e par!'.format(num))