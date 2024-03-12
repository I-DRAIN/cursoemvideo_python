''' Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequencia de Fibonacci
Ex: 0 1 1 2 3 5 8'''

n = int(input('Digite um numero qualquer: '))

print('Os {} primeiros termos da Sequencia de Fibonacci sao: '.format(n))

start = 0
print(start)

anterior = start
soma = 1
print(soma)



while n != 0:
    
    soma = soma + anterior
    print(soma)
    anterior = soma - anterior
    
    

    n -= 1


