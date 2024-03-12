### Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sao maiores.

s1 = 0
s2 = 0

year = 2023

for c in range(0,7):
    n = int(input('Digite o ano de nascimento: '))
    if year - n >= 21:
        s1 += 1
    else:
        s2 += 1

print('O numero de pessoas com mais de 21 anos e {} e o numero de pessoas com menos de 21 anos e {}'.format(s1,s2))



