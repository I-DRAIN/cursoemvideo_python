''' Crie um programa que leia o nome e o preco de varios produtos. O programa devera perguntar ao usuario se ele quer continuar ou nao.
No final mostre:
[a] Qual e o total gasto na compra.
[b] Quantos produtos custam mais de R$1000
[c] Qual e o nome do produto mais barato.'''

produto = ''
preco =  0
maisquemil= 0
total = 0
maisbarato = 100000000000000

while True:
    
    produto = str(input('Produto: '))
    preco = int(input('Preco: R$'))
    
    if preco > 1000:
        maisquemil += 1

    total = total + preco

    if preco < maisbarato:
        maisbarato = preco
        produtomaisbarato = produto
    final = str(input('Deseja continuar [S/N]? ')).upper()

    if final == 'N':
        break

print(f'Voce gastou R${total:.2f}')
print(f'A sua compra tem {maisquemil} produtos que custam mais de mil reais.')
print(f'O produto mais barato foi {produtomaisbarato}.')