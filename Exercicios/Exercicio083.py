''' Crie um programa onde o usuario digita uma expressao qualquer que use parenteses. Seu aplicativo devera analisar se a expressao passada esta com os parenteses abertos e fechados na ordem correta.'''

expressao = str(input('Digite a expressao: '))
abertos = []
fechados = []
for c in expressao:
    if c == '(':
        abertos.append(c)
    elif c == ')':
        fechados.append(c)

if len(abertos) == len(fechados):
    print('Sua expressao e valida!')
else:
    print('Sua expressao e invalida!')
