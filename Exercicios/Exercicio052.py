### Faca um programa que leia um numero inteiro e diga se ele e ou nao um numero primo.

n = int(input('Digite um numero inteiro: '))

special = 1
for c in range(2,n):
    resto = n%c
    if resto == 0:
        special = 0

if special == 0:
    print('Esse numero nao e primo!')
else:
    print('Esse numero e primo!')
    

