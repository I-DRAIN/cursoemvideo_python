''' Faca um programa que tenha uma funcao chamada contador(), que receba tres parametros: inicio, fim e passo e realize a contagem.
    Seu programa tem que realizar tres contagens atraves da funcao criada:
    
    a) De 1 ate 10, de 1 em 1.
    b) de 10 ate 0, de 2 em 2
    c) Uma contagem personalizada'''
from time import sleep

def contador(inicio, fim, passo):
    print('-'*20)
    print(f'Contagem de {inicio} ate {fim} de {passo} em {passo}')
    sleep(2.5)

    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(1/2)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ',flush=True)
            sleep(1/2)
            cont -= passo
        print('FIM!')
    

#Programa principal    
contador(1,10,1)
contador(10,0,2)
print('Agora e sua vez de personalizar a contagem!')

inicio = int(input('Qual e o inicio? '))
fim = int(input('Qual e o fim? '))
passo = int(input('Qual e o passo? '))
contador(inicio,fim,passo)


