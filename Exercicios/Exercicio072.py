''' Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero ate vinte.
    Seu programa devera ler um numero pelo teclado (entre 0 e 20) e mstra-lo por extenso.'''


numeros = ('zero','um', 'dois', 'tres', 'quatro', 'cinco',
            'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'catorze', 'quinze',
            'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

escolha = int(input('Digite um numero de 0 a 20: '))

while not escolha in range(0,20):
    escolha = int(input('Digite um numero de 0 a 20: '))

print(f'Voce digitou o numero {numeros[escolha]}')