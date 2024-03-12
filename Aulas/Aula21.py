help(print)
print('-'*60)
print(input.__doc__)
print('-'*60)

def contador(i,f,p):
    """
    -> Faz uma contagem e mostra na tela
        : param i: inicio da contagem
        : param f: fim da contagem
        : param p: passo da contagem
        : return: sem retorno
        
     """   
    c = i
    while c<f:
        print(f'{c}', end='..')
        c+=p
    print('FIM!')

contador(2,10,2)
print('-'*60)
help(contador)
print('-'*60)


def somar(a,b,c=0): #parametro opcional, o parametro C e opcional
    """
    -> Faz a soma de tres valores e mostra o resultado na tela
    : parametro a: o primeiro valor
    : parametro b: o segundo valor
    : parametro c: o terceiro valor
    Funcao criada por Luciano Alves de Oliveira

    """
    s = a+b+c
    print(f'A soma vale {s}.')



somar(3,2,5)
somar(4,8)
print('-'*60)

def teste():
    x = 8
    print(f'Na funcao teste, n vale {n}') # quando mostrado na tela, o valor de n recebe o valor de 2, declarado abaixo, pois tem escopo global (esta no programa principal)
    print(f'Na funcao teste, x vale {x}') # Nesse caso, o x tem escopo local pois esta declarado apenas na funcao. 

# Programa Principal

n=2
print(f'No programa principal, n vale {n}')
teste()
#print(f'No programa principal, x vale {x}')
print('-'*60)

def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')

n1 = 2
funcao()
print(f'N1 fora vale {n1}')
print('-'*60)


def somar(a=0,b=0,c=0):
    s = a+b+c
    return s

r1 = somar(3,2,5)
r2 = somar(2,2)
r3 = somar(6)

print(f'Meus calculos deram {r1}, {r2}, {r3}')
print('-'*60)

def fatorial(num = 1):
    f = 1
    for c in range(num,0,-1):
        f *= c
    return f

n = int(input('Digite um numero: '))
print(f'O fatorial de {n} e igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f'Os resultados sao {f1}, {f2}, {f3}')
print('-'*60)

def par(n=0):
    if n%2 ==0:
        return True
    else:
        return False

num = int(input('Digite um numero: '))
if par(num):
    print('E par!')
else:
    print('Nao e par!')