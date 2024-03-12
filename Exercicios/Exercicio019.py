# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faca um programa que o ajude lendo o nome deles e escrevendo o nome do escolhido

import random

aluno1 = str(input('Aluno 1: '))
aluno2 = str(input('Aluno 2: '))
aluno3 = str(input('Aluno 3: '))
aluno4 = str(input('Aluno 4: '))

escolha = random.choice([aluno1, aluno2, aluno3, aluno4])

print('O aluno escolhido foi {}. '.format(escolha))