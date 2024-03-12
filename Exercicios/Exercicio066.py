''' Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar 999.
No final, mostre quantos numeros foram digitados e qual foi a soma entre eles'''
count = 0
soma = 0

while True:
    n = int(input('Digite um numero (999 para parar): '))
    
    if n == 999:
        break

    soma += n
    count += 1

print(f'Voce digitou {count} numeros e a soma deles e de {soma}.')
