#Faca um algoritmo que leia o preco de um produto e mostre seu preco com 5% de desconto

preco = float(input('Digite o preco do produto: '))

desconto = preco*0.05
novopreco = preco - desconto

print('Originalmente o preco do produto era de {}. Com 5% de desconto, o novo preco e de {}.'
.format(preco,novopreco))