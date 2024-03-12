# Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preco da passagem, cobrando R$ 0.50 por Km 
# para viagens de ate 200Km e R$0.45 para viagens mais longas.
#

distance = int(input('A distancia da viagem e: '))

if distance <= 200:
    value = distance*0.50
    print('O valor da passagem e de R${:.2f}.'.format(value))
else:
    value = distance*0.45
    print('O valor da passagem e de R${:.2f}.'.format(value))
