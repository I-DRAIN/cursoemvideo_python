''' Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar o valor 999, que e a condicao de parada. No final
mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag)'''

n = 0

soma = 0
count = 0
n = int(input('Digite um numero [999 para]: '))
while n != 999:
    
    soma = soma + n
    count += 1
    n = int(input('Digite um numero [999 para]: '))

print('Voce digitou {} numeros e a soma entre eles foi de {}'.format(count,soma))