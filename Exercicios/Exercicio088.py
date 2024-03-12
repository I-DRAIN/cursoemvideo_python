''' Faca um programa que ajude um jogador da Mega Sena a criar palpites. O programa vai perguntar quantos jogos serao gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo,
    cadastrando tudo em uma lista composta'''
import random
import time 

jogo = list()
j = list()

print('-'*40)
print('{:^40}'.format('Jogo na MEGA SENA'))
print('-'*40)

jogos = int(input('Quantos jogos voce quer que eu sorteie? '))


print('-='*3, end= ' ')
print(f'SORTEANDO {jogos} JOGOS', end = ' ')
print('-='*3)

cont = 0
for count in range(0,jogos):
    while True:
        n = random.randint(1,60)
        if n not in j:
            j.append(n)
            cont +=1
        if cont >=6:
            break
    j.sort()
    jogo.append(j[:])
    j.clear()
    cont = 0

for c in range(0,len(jogo)):
    print(f'Jogo {c+1}: {jogo[c]}')
    time.sleep(1)

print('-='*5, end = ' ')
print('< BOA SORTE! >', end= ' ')
print('-='*5)


