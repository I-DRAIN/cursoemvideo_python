''' Faca um programa que leia nome media de um aluno, guardando tambem a situacao em um dicionario. No final, mostre o conteudo da estrutura na tela'''

aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))

if aluno['media'] > 7:
    aluno['Situacao'] = 'Aprovado'
else:
    aluno['Situacao'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} e igual a {v}')
