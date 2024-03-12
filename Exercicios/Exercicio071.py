''' Crie um programa que simule o funcionamento d eum caixa eletronico. No inicio, pergunte ao usuario qual sera o valor a ser sacado (numero inteiro) 
e o programa vai informar quantas cedulas serao entregues.
obs: Considere que o caixa possui cedulas de R$50, R$20, R$10 e R$1'''

print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)

valor = int(input('Quanto voce quer sacar? R$'))
total = valor
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced +=1
        
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R${ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break