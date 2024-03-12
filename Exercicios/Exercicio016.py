# Crie um programa que leia um numero real qualquer pelo teclado e mostre a sua porcao inteira
# Ex: Digite um numero: 6.127 O numero 6.127 tem a parte inteira 6.

num = float(input('Digite um numero: '))

new_num = num // 1

print('O numero {} tem a parte inteira {}'.format(num, new_num))
