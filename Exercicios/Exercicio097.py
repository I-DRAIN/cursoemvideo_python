''' Faca um programa que tenha uma funcao chamada escreva(), que receba um texto qualquer como parametro e mostre uma mensagem com tamanho adaptavel.
    Ex:
    escreva('Ola, Mundo!')

    ~~~~~~~~~~~
    Ola, Mundo!
    ~~~~~~~~~~~


'''

def escreva(mensagem):
    count = len(mensagem) + 4
    
    print('~'*count)
    print(f'  {mensagem}')
    print('~'*count)


mensagem = str(input('Digite sua mensagem: '))

escreva(mensagem)