''' Faca um programa que leia 5 valores numericos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectibas posicoes na lista'''


    
valores = []    
for count in range(0,5):
    valores.append(int(input('Digite um numero: ')))

print(valores)

maior = menor = valores[0]

for c in valores:
    if c >= maior:
        maior = c
    elif c < menor:
        menor = c

print(f'O maior valor digitado foi o {maior} e esta na posicao {valores.index(maior)}.')
print(f'O menor valor digitado foi o {menor} e esta na posicao {valores.index(menor)},')
