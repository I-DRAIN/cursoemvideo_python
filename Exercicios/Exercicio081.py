''' Crie um programa que vai ler varios numeros e colocar em uma lista.
Depois disso, mostre:
a) Quantos numeros foram digitados
b) A lista de valores ordenada de forma decrescente.
c) Se o valor 5 foi digitado e esta ou nao na lista'''

lista = []

while True:
    lista.append(int(input('Digite um numero: ')))
    print('Numero adicionado...')
    x = str(input('Deseja continuar? [S/N] ')).upper()

    if x == 'N':
        break

print(f'Foram digitados {len(lista)} numeros.')

lista.sort(reverse=True)
print(f'A lista em ordem decrescente e {lista}')

if 5 in lista:
    print(f'O valor 5 foi digitado na posicao {lista.index(5)}.')
else:
    print('O valor 5 nao foi digitado!')