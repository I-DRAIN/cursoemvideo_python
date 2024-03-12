### Desenvolva um prgrama que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.

s = 0
for c in range(0,6):
    n = int(input('Digite um numero inteiro: '))
    x = n%2
    if x == 0:
        s += n

print('A soma dos numeros pares que voce digitou e {}'.format(s))



