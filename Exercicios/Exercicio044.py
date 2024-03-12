# Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preco normal e condicao de pagamento
# a vista em dinheiro/cheque: 10% desconto
# a vista no cartao: 5% de desconto
# em ate 2x no cartao: preco normal
# 3x ou mais: 20% de juros

preco = float(input('Qual e o preco do produto? '))
metodo = str(input('Sera em dinheiro, cheque ou cartao? '))

if metodo == 'cartao':
    metodo2 = str(input('a vista, 2, 3 ou mais vezes? '))
    if metodo2 == 'a vista':
        novo_preco = preco - (preco*0.05)
        print('5% de desconto! O valor a pagar e R${}.'.format(novo_preco))
    elif metodo2 == '2':
        print('preco normal! O valor a pagar e R${}'.format(preco))
    else:
        novo_preco = preco*1.2
        print('20% de juros. O valor a pagar e de R${}'.format(novo_preco))
else:
    novo_preco = preco - (preco*0.05)
    print('Voce teve 10% de desconto! O valor a pagar e de R${}.'.format(novo_preco))