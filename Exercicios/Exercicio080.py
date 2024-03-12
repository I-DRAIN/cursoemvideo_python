''' Crie um programa onde o usuario possa digitar cinco valores numerios e cadastre-os em uma lista, ja na posicao correta de insercao sem usar o sort().
    No final, mostre a lista ordenada na tela.'''


valores = []

for c in range(0,5):
    x = int(input('Digite um numero: '))
    
    if c == 0 or x > valores[-1]:
        valores.append(x)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(valores):
            if x <= valores[pos]:
                valores.insert(pos,x)
                print(f'Adicionado na posicao {pos} da lista')
                break
                
            pos += 1 
    

    

    
      
   

print(valores)