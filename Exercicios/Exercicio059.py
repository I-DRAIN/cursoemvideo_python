''' Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa 
Seu programa devera realizar a operacao solicitada em cada caso'''

c = 0
resultado = 0
n1 = 0
n2 = 0


n1 = input('Digite um valor: ')
    

n2 = input('Digite outro valor: ')
    

while c != 5:
    print('Menu')
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos numeros')
    print('[5] sair do programa')


    c = int(input('O que voce deseja fazer: '))



    if c == 1:
        resultado = n1+n2
        print('A soma entre {} e {} e {}'.format(n1,n2,resultado))

    elif c == 2:
        resultado = n1*n2
        print('A multiplicacao entre {} e {} e de {}'.format(n1,n2,resultado))
    
    elif c == 3:
        if n1 > n2:
            print('O numero maior e {}'.format(n1))
        elif n2 > n1:
            print('O numero maior e {}'.format(n2))
        else:
            print('Os dois numeros sao iguais')
    elif c == 4:
        print('Okay! Novos numeros!')
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite outro valor'))
    
    elif c == 5:
        print('Finalizando!! Tchau Tchau')
        break

    else:
        print('Essa opcao e inexistente! Tente novamente.')


print('Foi um prazer trabalhar com voce!')