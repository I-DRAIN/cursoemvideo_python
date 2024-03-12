### Refaca o Desafio 009, mostrando a tabuada de um numero que o usuario escolher, so que agora utilizando um laco for.

n = int(input('Digite um numero: '))

print('A tabuada do {} e: '.format(n))

for c in range(0,11):
    t = c*n
    print('{} vezes {} e igual a {}'.format(n,c,t))