''' Faca um programa que jogue par ou impar com o computador. O jogo sera interrompido quando o jogador perder, mostrando o total de 
vitorias consecutivas que ele conquistou no final do jogo'''
from random import randint

print('=-'*20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*20)
count = 0
while True:
    n = int(input('Diga um valor: '))
    choice = str(input('Par ou Impar? [P/I] ')).upper()

    while choice not in 'IP':
        choice = str(input('Par ou Impar? [P/I] ')).upper()

    if choice == 'I':
        choice = 'IMPAR'
    else:
        choice = 'PAR'

    c = randint(1,11)
    soma = c+n

    if soma %2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'


    print(f'Voce jogou {n} e o computador jogou {c}. Total de {soma} deu {resultado}.')
    print('-'*40)

    if choice == resultado:
        print('Voce Venceu! Parabens')
        print('Vamos jogar novamente')
        print('=-'*20)
        count += 1
    else:
        print('Voce perdeu! Game Over')
        break
print(f'Voce ganhou {count} partidas')
