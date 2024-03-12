#Faca um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.

nome = str(input('Digite seu nome completo: '))

print(('O seu primeiro nome e {}'.format(nome.split()[0])))
print(('O seu ultimo nome e {}'.format(nome.split()[-1])))