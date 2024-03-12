# Refaca o desafio dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado:
# Equilatero, todos os lados iguais. Isosceles, dois lados iguais. Escaleno, todos os lados diferentes.

n1 = int(input('Digite um comprimento: '))
n2 = int(input('Digite outro comprimento: '))
n3 = int(input('Digite mais um comprimento: '))

if n1 + n2 > n3:
    if n1 + n3 > n2:
        if n2 + n3 > n1:
            print('E possivel formar um triangulo')
            if n1 == n2 == n3:
                print('Esse triangulo e equilatero!')
            elif n1 == n2 or n1 == n3 or n2 == n3:
                print('Esse triangulo e Isosceles!')
            else:
                print('Esse triangulo e Escaleno')
        else:
            print('Nao e possivel se formar um triangulo')
    else:
        print('Nao e possivel se formar um triangulo')

else:
    print('Nao e possivel se formar um triangulo')