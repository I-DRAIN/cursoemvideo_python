''' Aprimore o Desafio 93 para que funcione com varios jogadores, incluindo um sistema de visualizacao do aproveitamento de cada jogador'''



jogadores = list()
estatistica = dict()

while True:
    estatistica.clear()
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
    jogadores.append(estatistica.copy())

    while True:
        x = str(input('Deseja continuar [S/N]? ')).upper()[0]
        if x in 'SN':
            break
        else:
            print('ERRO!! So valores S ou N.')
    
    if x == 'N':
        print('-='*30)
        break
    else:
        print('-'*60)


print(f'{"cod":^4} {"nome":<15}{"gols":<15}{"total":<7}')
print('-'*60)    
for cont, valor in enumerate(jogadores):
    print(f'{cont:>3} ', end=' ')
    for d in valor.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*60)


while True:
    busca = (int(input('Mostrar dado de qual jogador? (999 para parar): ')))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO! Nao existe jogador com codigo {busca}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[busca]["nome"]}')
        for i, g in enumerate(jogadores[busca]["gols"]):
            print(f' No jogo {i} fez {g}')
    print('-'*60)
print('<<<VOLTE SEMPRE>>>')




    

