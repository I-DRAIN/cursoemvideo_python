''' Melhore o jogo do desafio 28 onde o computador vai pensar em um numero entre 0 e 10. So que agora o jogador vai tentar adivinhar ate acertar
mostrando quantos palpites foram necessarios para vencer'''

from random import randint
from time import sleep

n = randint(1,10)
g = 0
count = 0

print('Pensei em um numero...')
sleep(1)
print('Voce consegue adivinhar?')
sleep(1)

while g != n:
    g = int(input('Que numero eu pensei? '))
    print('Voce errou! Tente denovo!')
    count += 1



print('Correto! O numero que eu pensei foi {}. Voce precisou de {} tentativas para acertar.'.format(g,count))

