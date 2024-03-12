lanche = ('hamburguer', 'suco', 'pizza', 'pudim')

print(lanche[1])
print(lanche[0:2])

print(len(lanche))

for c in lanche:
    print(c)


for c in range(0,len(lanche)):
    print(c)
    print(lanche[c])
    print(f'Eu vou comer {lanche[c]} na posicao {c}')

print(lanche[:2])
print(lanche[2:])


for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')


print(sorted(lanche))

a = (2,5,4)
b = (5,8,1,2)
c = a + b
d = b + a

print(c)
print(d)

print(c.count(5))
print(c.index(8))

print(d.index(5,1))

pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)