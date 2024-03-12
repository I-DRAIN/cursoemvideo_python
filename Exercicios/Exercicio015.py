# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preco a pagar, sabendo que
# o carro custa R$60.00 por dia e R$0.15 por Km rodado

dias = int(input('Quantos dias? '))
Km = float(input('Quantos Kms? '))

preco = (dias*60)+(Km*0.15)

print('O valor final a pagar e de R${:.2f}'.format(preco))