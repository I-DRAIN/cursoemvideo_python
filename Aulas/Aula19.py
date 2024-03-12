pessoa = {'nome': 'Gustavo', 'sexo': 'M', 'idade': '22'}
print(pessoa['idade'])

print(f'O {pessoa["nome"]} tem {pessoa["idade"]} anos')

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

for k, v in pessoa.items():
    print(f'{k} = {v}')

print('=-'*40)

Brasil = list()
estado1 = {'uf':'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'Sao Paulo', 'sigla': 'SP'}

Brasil.append(estado1)
Brasil.append(estado2)

print(Brasil)
print(Brasil[0])
print(Brasil[1]['sigla'])

print('=-'*40)

estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O {k} tem {v}')