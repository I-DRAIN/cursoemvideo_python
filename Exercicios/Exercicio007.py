#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua media

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

media = (n1+n2)/2

print('A media entre {} e {} e de {}!'.format(n1,n2,media))