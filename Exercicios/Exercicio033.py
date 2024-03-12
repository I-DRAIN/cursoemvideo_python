# Faca um programa que leia tres numeros e mostre qual e maior e qual e menor.



n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite mais um numero: '))

order = [n1,n2,n3]
order.sort()

print('O menor numero e {}.'.format(order[0]))
print('O maior numero e {}.'.format(order[2]))


