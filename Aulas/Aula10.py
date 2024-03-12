#Condicoes

#nome = str(input('Qual e seu nome? '))

#if nome == 'Gustavo':
#    print('Que nome bonito!')
#else:
#    print('Que nome normal!')

#print('Bom dia, {}'.format(nome))

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

m = (n1+n2)/2

print('A sua media foi {:.1f}'.format(m))

if m >= 6:
    print('Sua media foi boa. Parabens!')
else:
    print('Sua media foi ruim. Estude mais!')