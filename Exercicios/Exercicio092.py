''' Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cdastre-os (com idade) em um dicionario.
    Se por acaso a CTPS for diferente de ZEO, o dicionario recebera tambem o ano da contratacao e o salario.
    Calcule e acrescente, alem da idade, com quantos anos a pssoa vai se aposentar'''
from datetime import datetime
cadastro = dict()

cadastro['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
cadastro['idade'] = datetime.now().year - nasc
cadastro['ctps'] = int(input('Carteira de Trabalho (0 nao tem): '))

if cadastro['ctps'] != 0:
    cadastro['contratacao'] = int(input('Ano de Contratacao: '))
    cadastro['salario'] = int(input('Salario: R$ '))
    cadastro['aposentadoria'] = cadastro['contratacao'] + 35 - nasc

print('-='*70)
print(cadastro)
for k, v in cadastro.items():
    print(f'{k} tem o valor de {v}')

