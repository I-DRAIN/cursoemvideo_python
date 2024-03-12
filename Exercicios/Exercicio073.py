''' Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro, na ordem de colocacao. Depois mostre:
    a) Apenas os 5 primeiros colocados.
    b) Os ultimo 4 colocados.
    c) Uma lista com os times em ordem alfabetica.
    d) Em que posicao na tabela esta o time do Corinthians'''

tabela = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians',
            'Flamengo', 'Athletico', 'Atletico MG', 'Fortaleza',
            'Sao Paulo', 'America MG', 'Botafogo', 'Santos',
            'Goias', 'Bragantino', 'Coritiba', 'Cuiaba',
            'Ceara', 'Atletico GO', 'Avai', 'Juventude')

print(tabela[:5])
print(tabela[-4:])
print(sorted(tabela))

pos = tabela.index('Corinthians')
print(pos+1)