# Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento
#Para salarios superiores a R$ 1250.00, calcule um aumento de 10%
# Para salarios inferiores, o aumento e de 15%

salario = float(input('Qual o salario? '))

if salario > 1250:
    new_sala = 1.1*salario
    print('O novo salario e de R${:.2f}.'.format(new_sala))
else:
    new_sala = 1.15*salario
    print('O novo salario e de R${:.2f}.'.format(new_sala))
    