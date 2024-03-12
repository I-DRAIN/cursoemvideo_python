''' Crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista.
    Caso o nmero ja exista la dentro, ele nao sera adicionado. No final, serao exibidos todos os valores unicos digitados em ordem crescente'''

termino = False
valores = []

while termino == False:
    numero = int(input('Digite um valor: '))
    if numero in valores:
        print('Valor duplicado! Nao vou adicionar...')
    else:
        valores.append(numero)
        print('Valor adicionado com sucesso...')
    x = str(input('Deseja continuar? [S/N] ')).upper()

    if x == 'N':
        break
valores.sort()
    
print(f'Voce digitou os valores {valores}.')
