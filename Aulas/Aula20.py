def lin():
    print('-'*30)

a = 4
b = 5
s = a + b


lin()

a = 8
b = 9
s = a + b


print(lin)

a = 2
b = 1
s = a + b

print(s)
print(lin)
#funcao
def soma(a,b):
    print(f'o A = {a} e o b = {b}.')
    s = a + b
    print(f'A soma vale {s}')


#programa principal
soma(4,5)
soma(b=8,a=9)
soma(1,2)
lin()

def contador(*num):
    tam = len(num)
    print(f'recebi os valores {num} e sao ao todo {tam} numeros')
    for val in num:
        print(f'{val}')
    print('FIM')


contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)

lin()

def dobra(lst):
    pos = 0
    while pos<len(lst):
        lst[pos]*=2
        pos+=1

valores = [6,3,9,1,0,2]

print(valores)
dobra(valores)
print(valores)

lin()

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5,2)
soma(2, 9, 4)



