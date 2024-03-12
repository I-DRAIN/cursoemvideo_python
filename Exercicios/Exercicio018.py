# Faca um programa que leia um angulo qualquer e 
# mostre na tela o valor do seno, cosseno e tangente desse angulo

import math

angulo = float(input('Qual e o angulo? '))
angulo2 = math.radians(angulo)

sin = math.sin(angulo2)
cos = math.cos(angulo2)
tan = math.tan(angulo2)

print('O cosseno de {} e {:.3f}'.format(angulo,cos))
print('O seno de {} e {:.3f}'.format(angulo,sin))
print('A tangente de {} e {:.3f}'.format(angulo,tan))