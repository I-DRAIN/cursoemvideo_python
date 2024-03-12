# Escreva um programa que leia o ano de nascimento de um jovem e informe:
# Se ele ainda vai se alistar no servico militar
# Se e hora de se alistar
# Se ja passou do tempo de se alistar
# Seu programa tambem devera mostrar quanto tempo falta ou se passou do prazo

aniversario = int(input('Qual ano voce nasceu? '))
ano = int(input('Qual o ano de hoje? '))

idade = ano-aniversario

if idade > 18:
    prazo = idade - 18
    print('Voce tem {} anos. Voce esta ha {} anos atrasado em se alistar!'.format(idade, prazo))
elif idade == 18:
    print('Voce deve se alistar!')
else:
    prazo = 18 - idade
    print('Voce tem {} anos. Faltam {} anos para voce se alistar!'.format(idade, prazo))