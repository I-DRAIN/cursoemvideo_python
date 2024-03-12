### Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
### a) A media de idade do grupo
### b) O nome do homem mais velho
### c) Quantas mulheres tem menos de 20 anos.

idade = 0
idadeHomemVelho = 0
counter = 0
nome = ''

for c in range(0,4):
    nome1 = input('Digite o nome: ')
    sexo1 = input('Sexo (F/M): ')
    idade1 = int(input('Idade: '))

    idade += idade1

    if sexo1 == 'M' and idade1 > idadeHomemVelho:
        nome = nome1
    
    if sexo1 == 'F' and idade1 < 20:
        counter += 1

print('A media de idade desse grupo e {}.'.format(idade/4))
print('O nome do homem mais velho e {}'.format(nome))
print('Ha {} mulher(es) com menos de 20 anos.'.format(counter))
