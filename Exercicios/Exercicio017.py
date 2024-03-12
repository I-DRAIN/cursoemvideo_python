#Faca um programa que leia o cateto oposto e o cateto adjacent de um triangulo retangulo,
#  calcule e mostre o comprimento da hipotenusa

import math

co = float(input('Qual e o cateto oposto? '))
ca = float(input('Qual e o cateto adjacente? '))

hyp = math.sqrt(co**2 + ca**2)

print('A hypotenusa eh {}'.format(hyp))