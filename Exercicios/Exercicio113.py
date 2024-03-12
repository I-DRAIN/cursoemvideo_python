""" Reescreva a funcao leiaInt() que fizemos no desafio 104, incluindo a possibilidade da digitacao de um numero de tipo invalido. Aproveite e crie tambem uma funcao leiaFloat() com a 
mesma funcionalidade."""
def main():
    n = leiaInt('Digite um numero inteiro: ')
    f = leiaFloat('Digite um numero real: ')
    print(f'Voce acabou de digitar os numeros {n} e {f}')
    

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um numero inteiro valido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mEntrada de dados interrompida pelo usuario.\033[m')
            return 0
        else:
            return n
            

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um numero inteiro valido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mEntrada de dados interrompida pelo usuario.\033[m')
            return 0
        else:
            return n
        

main()
