#Faca um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que
#cada litro de tinta pinta uma area de 2m2.

largura = float(input('Digite a altura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = largura*altura

litro = area/2

print('A quantidade de tinta necessaria para se pintar {} m2 e de {} litros.'.format(area,litro))