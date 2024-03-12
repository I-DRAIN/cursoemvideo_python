''' Crie um progrAma que vai gerar 5 numeros aleatorios e colocar em uma tupla. Depois disso mostre a listagem dos numeros gerados e tbm indique o menos e o maior valor que estao na tupla'''

x1 = int(input('Digite um numero: '))
x2 = int(input('Digite outro numero: '))
x3 = int(input('Digite outro numero: '))
x4 = int(input('Mais um numero: '))
x5 = int(input('Ultimo numero: '))

numeros = (x1,x2,x3,x4,x5)

numeros = sorted(numeros)

print(f'O maior numero digitado foi o {numeros[-1]}')
print(f'O menor numero digitado foi o {numeros[0]}')