''' Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
    Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso sera guardado em um dicionario, incluindo o total de gols feitos durante o campeonato'''

estatistica = dict()

estatistica['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {estatistica["nome"]} jogou? '))
gols = list()

for i in range(0,partidas):
    gols.append(int(input(f'Quantos gols na partida {i}? ')))

estatistica['gols'] = gols[:]
soma = 0
for i in gols:
    soma += i

estatistica['total'] = soma

print('-='*50)
print(estatistica)
print('-='*50)

for k,v in estatistica.items():
    print(f'O campo {k} tem valor {v}.')
print('-='*50)

print(f' O Jogador {estatistica["nome"]} jogou {partidas} partidas.')
for i in range(0,5):
    print(f'   => Na partida {i}, fez {gols[i]}.')
print(f'Foi um total de {soma} gols')