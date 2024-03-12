''' Crie um programa que leia varios numeros inteiros pelo teclado. No final da execucao, mostre a media entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar se ele quer ou nao continuar a digitar valores.'''


soma = 0
count = 0
maior = 0
menor = 1000000000000000000

answer = 'S'


while answer == 'S':
    n = int(input('Digite um numero: '))
    
    

    soma += n
    count += 1


    if n > maior:
        maior = n
    
    elif n < menor:
        menor = n

    answer = str(input('Voce deseja continuar? [S/N] ')).upper()


print('A soma destes numeros foi de {}.'.format(soma))
print('A media entre eles foi de {}.'.format(soma/count))
print('O maior numero digitado foi de {}.'.format(maior))
print('O menor numero difgitado foi de {}.'.format(menor))