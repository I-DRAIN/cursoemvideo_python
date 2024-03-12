''' Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada o programa dvera perguntar se o usuario quer ou nao continuar.
Ao final, mostre 
[a] quantas pessoas tem mais de 18 anos
[b] quantos homens foram cadastrados
[c] quantas mulheres tem menos de 20 anos'''

man = 0
womenu20 = 0
age = 0

while True:
    age = int(input('Digite a idade:'))
    
    gender = str(input('Digite o sexo [M/F]: ')).upper()
    while not gender in 'MmFf':
        gender = str(input('Digite o sexo [M/F]: ')).upper()
    
    
    if gender == 'M':
        man = man + 1

        
    if gender == 'F':
        if age < 20:
            womenu20 += 1
    
    
    final = str(input('Deseja continuar [S/N]? '))
    while not final in 'SsNn':
        final = str(input('Deseja continuar [S/N]? '))
    if final in 'Nn':
        break

print(f'O numero de mulheres com menos de 20 anos e de {womenu20}')
print(f'O numero de homens e de {man}')