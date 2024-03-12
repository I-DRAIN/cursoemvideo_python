# A confederacao nacional de Natacao precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria
# Ate 9 anos, Mirim. Ate 14 anos, Infantil. Ate 19 anos, Junior. Ate 20 anos, Senior. Acima, Master.

nascimento = int(input('Que ano o atleta nasceu? '))
ano = int(input('Que ano e hoje? '))

idade = ano-nascimento

if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JUNIOR ')
elif idade <= 20:
    print('Categoria: SENIOR')
else:
    print('Categoria: MASTER')