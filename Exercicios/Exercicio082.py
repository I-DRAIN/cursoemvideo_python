''' Crie um programa que vai ler varios numeros e colocar em uma lista.
    Depois disso, crie duas listas extras que vao conter apenas os numeros pares e os impares, respectivamente.
    Ao final, mostre o conteudo das tres listas geradas.'''


lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Digite um numero: ')))
    print('Numero adicionado...')
    x = str(input('Deseja continuar? [S/N] ')).upper()
    if x == 'N':
        break

for c in lista:
    z = c%2
    if z == 0:
        pares.append(c)
    else:
        impares.append(c)
print('=-'*30)
print(f'A lista geral e {lista}.')
print(f'A lista dos numeros pares e {pares}.')
print(f'A lista dos numeros impares e {impares}.')