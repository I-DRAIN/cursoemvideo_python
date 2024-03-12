''' Faca um programa que leia um numero qualquer e mostre o seu fatorial Ex: 5! = 5x4x3x2x1 = 120'''




n = int(input('Digite um numero: '))
ni = n
r = n

if n == 0:
    print('O fatorial de 0 e 1')

else:
    while n > 0:
        
        if n-1 > 0:
            r = r * (n-1)
            n -= 1
            
        else:
            break

    
    
    print('O fatorial de {} e {}'.format(ni,r))