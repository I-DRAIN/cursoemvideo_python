#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

n1 = int(input('Digite um numero: '))

n2 = n1*2
n3 = n1*3
raiz = n1**(1/2)

print('O dobro de {} e {}. O triplo de {} e {}. A sua raiz quadrade e {}!'.format(n1,n2,n1,n3,raiz))