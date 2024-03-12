''' Crie um programa que tenha uma tupla com varias palavras (sem usar acentos). Depois disso, voce deve mostrar para cada palavra quais sao suas vogais.'''

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

vogais = 'aeiou'
letras = ''

for count in palavras:
    for c in count:
        if c in vogais:
            letras = letras + c + ' '
        
    print(f'Na palavra {count} temos {letras}.', end = ' ')
    print('')
    letras = ''
