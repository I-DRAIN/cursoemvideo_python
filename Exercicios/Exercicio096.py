''' faca um programa que tenha uma funcao chamada area(), que receba as dimensoes de um terreno retangular (largura e comprimento) e mostre a area do terreno. '''

def area(l,w):
    a = l*w
    
    print(f' A Area de um terreno {l}x{w} e de {a}m2.')


print('Controle de Terrenos')
print('-'*25)
l = float(input('LARGURA (m): '))
w = float(input('COMPRIMENTO (m): '))

area(l,w)
