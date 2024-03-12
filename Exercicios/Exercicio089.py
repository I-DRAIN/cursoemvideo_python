''' Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta. No final, 
    mostre um boletim contendo a media de cada um e permita que o usuario possa mostrar as notas de cada aluno individualmente'''

lista = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    lista.append([nome,[nota1, nota2],media])
    
    
    
    x = str(input('Deseja continuar? [S/N] ')).upper()
    if x == 'N':
        break

print('=-'*30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*26)


for cont, valor in enumerate(lista):
    print(f'{cont:<4}{valor[0]:<10}{valor[2]:>8.1f}')

print('-'*30)

while True:
    x = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if x == 999:
        print('FINALIZANDO...')
        print('<<< VOLTE SEMPRE >>>')
        break
    else:
        print(f'Notas de {lista[x][0]} sao {lista[x][1]}.')
     
    

    
    
    