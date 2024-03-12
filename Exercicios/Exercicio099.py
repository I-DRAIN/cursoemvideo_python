''' Faca um programa que tenha uma funcao chamada maior(), que recebe varios parametros com valores inteiros.
    Seu programa tem que analisar todos os valores e dizer qual deles e o maior '''
from time import sleep

def maior(*num):
    maior = 0
    for i in num:    
        if i > maior:
            maior = i
    print('-='*30)
    print('Analisando os valores passados...')
    for i in num:
        print(f'{i} ',end='', flush=True)
        sleep(0.3)
    
    print(f'Foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {maior}.')
    



maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()