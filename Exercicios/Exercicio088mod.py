import random
import time 

jogo = list()
j = list()

print('-'*40)
print('{:^40}'.format('Jogo na MEGA SENA'))
print('-'*40)

jogos = int(input('Quantos jogos voce quer que eu sorteie? '))

for i in range(0,4):
    print('-='*3, end= ' ')
    print(f'SORTEEI {jogos} JOGOS', end = ' ')
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

    #for c in range(0,len(jogo)):
    #    print(f'Jogo {c+1}: {jogo[c]}')


    #print('-='*5, end = ' ')
    #print('< BOA SORTE! >', end= ' ')
    #print('-='*5)

    cont = 0
    sorteio = list()
    while True:
        n = random.randint(1,60)
        if n not in sorteio:
            sorteio.append(n)
            cont += 1
        if cont >=6:
            break
    sorteio.sort()

    print(f'Os numeros sorteados no concurso foram {sorteio}.')
    print('-='*30)



    nada = um_acerto = dois_acertos = tres_acertos = quatro_acertos = cinco_acertos = tudo = 0
    acertos = 0

    for c in range(0,len(jogo)):
        for count in jogo[c]:
            if count in sorteio:
                acertos += 1
        
        if acertos == 0:
            nada +=1
            acertos = 0
        elif acertos == 1:
            um_acerto +=1
            acertos = 0
        elif acertos == 2:
            dois_acertos +=1
            acertos = 0
        elif acertos == 3:
            tres_acertos +=1
            acertos = 0
        elif acertos == 4:
            quatro_acertos +=1
            acertos = 0
        elif acertos == 5:
            cinco_acertos +=1
            acertos = 0
        elif acertos == 6:
            tudo +=1
            acertos = 0
                
        

    print(f' 0: {nada}')
    print(f' 1: {um_acerto}')
    print(f' 2: {dois_acertos}')
    print(f' 3: {tres_acertos}')
    print(f' 4: {quatro_acertos}')
    print(f' 5: {cinco_acertos}')
    print(f' 6: {tudo}')

