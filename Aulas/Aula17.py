num = [2,5,9,1]
num[2] = 3
num.append(7)
num.sort()
num.sort(reverse=True)
print(num)

num.insert(2,2)
print(num)
num.pop(1)
print(num)
num.remove(2)
print(num)
print(f'Essa lista tem {len(num)} elementos.')

if 5 in num:
    num.remove(5)
else:
    print('Nao achei o numero 4')


valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

print(valores)
for c, v in enumerate(valores):
    print(f'Na posicao {c} encontrei o valor {v}')

a = [2,3,4,7]
b = a[:]
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')

