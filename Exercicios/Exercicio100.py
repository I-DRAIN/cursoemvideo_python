''' faca um programa que tenha uma lista chamada numeros e duas funcos chamadas sorteia() e somaPar().
    A primeira vai sortear 5 numeros e vai coloca-los dentro da lista e a segunda vai mostrar a soma entre todos os valores pares sorteados pela funcao anterior.'''

from random import randint
from time import sleep



def sorteia(numeros):
    
    for i in range(0,5):
        x = randint(0,9)
        numeros.append(x)
    print('Sorteando 5 valores da lista: ', end='')
    for i in numeros:
        print(f'{i}', end=' ',flush=True)
        sleep(0.3)
    print('PRONTO!')
    return(numeros)
    
def somaPar(numeros):
    soma = 0
    for i in numeros:
        if i%2 == 0:
            soma+=i
    print(f'A soma dos numeros pares de {numeros}, temos {soma}.')





#Main Program
numeros = list()
sorteia(numeros)
somaPar(numeros)