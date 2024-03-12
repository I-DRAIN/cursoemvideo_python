### faca um programa que calcule a soma de todos os numeros impares que sao multiplos de tres e que se encontram no intervalo de 1 ate 500.

s = 0

for c in range(0,500):
    x = c%3
    y = c%2
    if x == 0 and y != 0:
        s += c

print(s)