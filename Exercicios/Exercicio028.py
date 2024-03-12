#Escreva um programa que faca o computador pensar um numero inteiro entre 0 e 5 e peca para o usuario tentar adivinhar o numero
# O programa devera mostrar na tela se o usuario acertou ou nao

import random

num = random.randint(0,5)
guess = int(input('Tente adivinhar um numero de 0 a 5 que estou pensando: '))

if guess == num:
    print('Voce acertou! O numero era {}!'.format(num))
else:
    print('Errou!! O numero era {}.'.format(num))
