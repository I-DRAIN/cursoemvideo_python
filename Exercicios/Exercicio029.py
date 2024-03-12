# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele
# foi multado. A multa vai custar R$ 7.00 por cada Km acima do limite

speed = float(input('Qual a velocidade? '))

if speed >= 80:
    multa = (speed - 80)*7
    print('Voce foi multado. Sua multa sera de R${:.2f}'.format(multa))
else:
    print('Voce nao foi multado')