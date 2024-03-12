### Desenvolva um programa que leia o primeiro termo e a razao de uma PA. No final, mostre os 10 primeiros termos dessa progressao.

n = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razao dessa PA: '))

top = (r*10)+n

for c in range(n,top,r):
    print(c)

