# O mesmo professor do desafio anterior quer sortear a ordem de apresentacao dos alunos.
# Faca um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

import random

aluno1 = str(input('Aluno 1: '))
aluno2 = str(input('Aluno 2: '))
aluno3 = str(input('Aluno 3: '))
aluno4 = str(input('Aluno 4: '))

ordem = random.sample([aluno1, aluno2, aluno3, aluno4], k=4)

#print(ordem[3])
print('A ordem de apresentacao sera {}, depois {}, depois {} e finalmente {}.'.format(ordem[0],ordem[1],ordem[2],ordem[3]))