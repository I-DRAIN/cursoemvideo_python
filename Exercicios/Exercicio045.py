#Faca um programa que faca o computador jogar jokempo com voce
import random
from time import sleep

options = ['papel', 'pedra', 'tesoura']
print('Vamos jogar JOKEMPO!')
print('Vou escolher... ESCOLHI!')

pc = random.choice(options)

voce = str(input('Sua vez: '))

print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PO!')
sleep(1)

print('-='*17)
if pc == 'papel' and voce == 'pedra':
    print('Eu escolhi papel! Eu ganhei!! :D')
elif pc == 'papel' and voce == 'tesoura':
    print('Eu escolhi papel! Voce ganhou! :(')
elif pc == 'papel' and voce == 'papel':
    print('Nos dois escolhemos papel. Vamos jogar novamente!')

elif pc == 'pedra' and voce == 'tesoura':
    print('Eu escolhi pedra! Eu ganhei!! :D')
elif pc == 'pedra' and voce == 'papel':
    print('Eu escolhi pedra! Voce ganhou! :(')
elif pc == 'pedra' and voce == 'pedra':
    print('Nos dois escolhemos pedra. Vamos jogar novamente!')

elif pc == 'tesoura' and voce == 'papel':
    print('Eu escolhi tesoura! Eu ganhei!! :D')
elif pc == 'tesoura' and voce == 'pedra':
    print('Eu escolhi tesoura! Voce ganhou! :(')
else:
    print('Nos dois escolhemos tesoura. Vamos jogar novamente!')
print('-='*17)



