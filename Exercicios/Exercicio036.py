# Escreva um programa para aprovar um emprestimo bancario para a compra de uma casa. O programa vai perguntar 
#o valor da casa, o salario do comprador, e em quantos anos ele vai pagar
#Calcule o valor da prestacao mensal sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado.

casa = int(input('Qual o valor da casa: '))
salario = int(input('Qual o seu salario mensal: '))
tempo = int(input('Em quanto tempo voce quer pagar (em anos)? '))

prestacao = casa/(tempo*12)
limite = salario*0.3

if prestacao > limite:
    print('Voce excedeu o limite de 30% do seu salario. Emprestimo nao aprovado')
    print(limite)
    print(prestacao)
else:
    print('Emprestimo aprovado! Sua prestacao sera de R${:.2f}.'.format(prestacao))