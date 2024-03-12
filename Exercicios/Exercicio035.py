# Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo.

r1 = float(input('Digite o comprimento de uma reta: '))
r2 = float(input('Digite o comprimento de outra reta: '))
r3 = float(input('Digite o comprimento de mais uma reta: '))

if r1+r2>r3:
    if r1+r3>r2:
        if r2+r3>r1:
            print('Esse triangulo existe!')
        else:
            print('Esse triangulo nao existe!')
    else:
        print('Esse triangulo nao existe!')
else:
    print('Esse triangulo nao existe!')