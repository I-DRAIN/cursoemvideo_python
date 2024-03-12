#Operadores Aritmeticos

#nome = input('Qual e seu nome? ')

#print('Prazer em te conhecer, {:=^20}'.format(nome))

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2

print('A soma e {},\n o produto e {}\n  e a divisao e {:.3f}!'.format(s,m,d),end='')
print('A divisao inteira e {} e a potencia e {}'.format(di,e))