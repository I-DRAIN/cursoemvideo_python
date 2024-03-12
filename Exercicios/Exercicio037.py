# Escreva um programa que leia um numero inteiro qualquer e peca para o usuario escolher qual sera a base de conversao:
# 1 para binario
#2 para octal
# 3 para hexadecimal

x = int(input("Digite um numero: "))
choice = int(input("""Voce quer transformar para:
[1] binario
[2] octal
[3] hexadecimal 
Escolha: """))

if choice == 1:
    y = bin(x)
    print('O numero {} em binario e {}'.format(x,y[2:]))
elif choice == 2:
    y = oct(x)
    print('O numero {} em octal e {}'.format(x,y[2:]))
elif choice == 3:
    y = hex(x)
    print('O numero {} em hexadecimal e {}'.format(x,y[2:]))
else:
    print('Numero invalido! Tente novamente!')