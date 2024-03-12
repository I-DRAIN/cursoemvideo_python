''' Crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados de casa pessoa em um dicionario e todos os dicionarios em uma lista.
    No final, mostre:
    a) Quantas pessoas foram cadastradas
    b) A media de idade do grupo
    c) Uma lista com todas as mulheres
    d) Uma lista com todas as pessoas com idade acima da media'''

pessoa = dict()
lista = list()
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO Por favor, digite apenas M ou F')
    
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    
    x = str(input('Quer continuar? [S/N] ')).upper()[0]
    
    lista.append(pessoa.copy())
    
    
    while True:
        if x in 'SN':
            break
    if x == 'N':
        break
print('-='*50)

print(f'- O grupo tem {len(lista)} pessoas.')

media = soma/len(lista)

print(f'- A media de idade do grupo de de {media:5.2f} anos.')
print(f'- As mulheres cadastradas foram ',end='')

for p in lista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()

print('- Lista das pessoas que estao acima da media: ', end='')
for p in lista:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()
print('<< ENCERRADO >>')
