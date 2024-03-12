''' Melhore o desafio 61, perguntando para o usuario se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.'''

n = int(input('Qual o primeiro termo da PA: '))
r = int(input('Qual a razao da PA: '))

count = 0

while count < 10:
    top = n + (r*count)
    print(top)
    count += 1



finish = 1

while finish != 0:
    c = int(input('Quantos termos a mais voce quer ver? '))
    x = c
    finish = c

    while x != 0:
        top = top+r
        print(top)
        x -= 1    

print('Programa encerrado! Obrigado!')

