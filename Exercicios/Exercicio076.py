''' Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos precos na sequencia.
    No final, mostre uma listagem de precos, organizando os dados de forma tabular'''

produtos = ('Lapis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.90)

print('='*40)
print('{:^40}'.format('PRODUTOS'))
print('='*40)

c = 0
while c in range(0,len(produtos)):
    print(f'{produtos[c]:.<30}R${produtos[c+1]:>7.2f}')
    c += 2

print('='*40)