""" Faca um programa que tenha uma funcao chamada ficha(), que receba dois parametros opcionais: o nome de um jogador e quantos gols ele marcou. O programa devera ser capaz
de mostar a ficha do jogador, mesmo que algum dado nao tenha sido informado corretamente"""

def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} marcou {gol} gols no campeonato')

# Programa principal
n = str(input('Qual o nome do jogador? ')).strip()
g = str(input('Quantos gols ele marcou? '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n == '':
    ficha(gol=g)
else:
    ficha(n,g)
    
