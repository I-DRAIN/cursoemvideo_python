# Faca um programa que leia uma frase e mostre:
# Quantas vezes aparece a letra 'a'
# Em que posicao ela aparece a primeira vez
# Em que posicao ela aparece pela ultima vez

frase = str(input(('Digite uma frase: ')))

print(frase.count('a'))
print((frase.index('a'))+1)
print((frase.rindex('a'))+1)