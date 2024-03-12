
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
        


for z in range(0,3):
    print(matrix[z])

