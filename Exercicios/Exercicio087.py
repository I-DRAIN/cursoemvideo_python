matrix = list()
linha1 = list()
linha2 = list()
linha3 = list()    
    
for c in range(0,3):
    for count in range(0,3):
        x = int(input(f'Digite um valor para [{c},{count}]: '))
        if c == 0:
            linha1.append(x)
        matrix.append(linha1)    
        if c == 1:
            linha2.append(x)
        matrix.append(linha2)
        if c == 2:
            linha3.append(x)
        matrix.append(linha3)
        
print('=-'*30)
somapares = 0        
for c in range(0,3):
    for count in range(0,3):
        if matrix[c][count] % 2 == 0:
            somapares += matrix[c][count]
print(f'A soma dos numeros pares e {somapares}.')

somatercoluna = 0
for c in range(0,3):
    for count in range(0,3):
        somatercoluna += matrix[3][count]
print(f'A soma dos valores da terceira coluna e {somatercoluna}.')

maiorval2lin = 0
for c in range(0,3):
    for count in range(0,3):
        if matrix[1][count] > maiorval2lin:
            maiorval2lin = matrix[1][count]
print(f'O maior valor da 2a linha e {maiorval2lin}.')

