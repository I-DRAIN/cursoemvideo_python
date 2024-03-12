''' Crie um programa onde o usuario possa digitar sete valores numericos e cadastre-os em uma lista unica que mantenha separado os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente.'''

lista = list()
pares = list()
impares = list()
lista.append(pares)
lista.append(impares)

for c in range(1,8):
    x = int(input(f'Digite o {c}o. valor: '))

    if x%2 == 0:
        pares.append(x)
    else:
        impares.append(x)

lista[0].sort()
lista[1].sort()

print('=-'*30)

print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores impares digitados foram: {lista[1]}')