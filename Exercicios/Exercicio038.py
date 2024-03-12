# Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor e maior
# O segundo valor e maior
# Nao existe valor maior, os dois sao iguais

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite mais um numero: '))

if n1 > n2:
    print('O primeiro e maior!')
elif n2 > n1:
    print('O segundo e maior!')
else:
    print('Nao existe valor maior, os dois sao iguais')