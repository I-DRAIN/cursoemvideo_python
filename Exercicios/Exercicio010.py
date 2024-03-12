#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira 
# e mostre quantos dolares ela pode comprar

dinheiro = float(input('Quanto dinheiro ha na carteira: R$'))

dolar = dinheiro/5.29

print('Com R${:.2f} voce pode comprar US${:.2f} dolares!'.format(dinheiro, dolar))
