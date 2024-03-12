''' Faca um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista. No final, mostre:
    a) Quantas pessoas foram cadastradas.
    b) Uma listagem com as pessoas mais pesadas.
    c) Uma listagem com as pessoas mais leves'''

pessoas = list()
individuo = list()
p = 0
pesomaior = pesomenor = 0


while True:
    individuo.append(str(input('Nome: ')))
    individuo.append(float(input('Peso: ')))
    pessoas.append(individuo[:])
    
    if p == 0:
        pesomaior = individuo[1]
        pesomenor = individuo[1]
    else:
        if individuo[1] > pesomaior:
            pesomaior = individuo[1]
        if individuo[1] < pesomenor:
            pesomenor = individuo[1]
        
    p += 1

    individuo.clear()

    
    x = str(input('Deseja continuar? [S/N] ')).upper()


    if x == 'N':
        break

maispesados = list()
maisleves = list()

for c in range(0,len(pessoas)):
    if pessoas[c][1] == pesomaior:
        maispesados.append(pessoas[c][0])
    elif pessoas [c][1] == pesomenor:
        maisleves.append(pessoas[c][0])



print(f'Ao todo voce cadastrou {p} pessoas.')

print(f'O maior peso cadastrado foi de {pesomaior}. Peso de {maispesados}.')
print(f'O menor peso cadastrado foi de {pesomenor}. Peso de {maisleves}.')
