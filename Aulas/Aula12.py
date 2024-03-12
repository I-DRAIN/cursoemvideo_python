# Condicoes aninhadas

nome = str(input('Qual e o seu nome? '))

if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'Pedro' or nome == 'Paulo':
    print('Seu nome e bem popular no Brasil!')
elif nome in 'Ana Claudia Jessica Juliana Isabella':
    print('Que belo nome feminino!')
else:
    print('Seu nome e tao normal!')
print('Bom dia, {}.'.format(nome))