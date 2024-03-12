### faca um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

Pmax = 0
Pmin = 0

for c in range(0,5):
    n = float(input('Digite o peso: '))
    if n > Pmax:
        Pmax = n
    else:
        Pmin = n

print('O maior peso e de {} e o menor peso e de {}'.format(Pmax,Pmin))
