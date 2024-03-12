#Faca um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
# Ex: Digite um numero: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

num = str(input('Digite um numero (0-9999): '))

print('unidade: {}'.format(num[3]))
print('dezena: {}'.format(num[2]))
print('centena: {}'.format(num[1]))
print('milhar: {}'.format(num[0]))