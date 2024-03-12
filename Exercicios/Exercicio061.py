''' refaca o desafio 051, lendo o primeiro termo e a razao de uma PA, mostrando os 10 primeiros termos da progressao usando o while'''

n = int(input('Qual o primeiro termo da PA: '))
r = int(input('Qual a razao da PA: '))

count = 0

while count < 10:
    top = n + (r*count)
    print(top)
    count += 1