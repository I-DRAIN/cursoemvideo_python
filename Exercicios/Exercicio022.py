#Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiusculas
# O nome com todas as letras minusculas
# Quantas letras ao todo sem considerar os espacos
# Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: '))

print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ','')))

dividido = nome.split()
print(len(dividido[0]))
