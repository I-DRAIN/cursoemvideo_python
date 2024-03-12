### Crie um programa que leia uma frase qualquer e diga se ela e um palindromo, desconsiderando os espacos

n = input('Digite uma frase: ')

n = n.replace(' ','')
print(n)

r = ''
for c in range(len(n),0,-1):
    r = r+n[c-1]

if r == n:
    print('Essa frase e um palindromo!')

else:
    print('Essa frase nao e um palindromo!')

