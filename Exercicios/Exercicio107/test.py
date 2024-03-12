import moeda

p = float(input('Digite o preco R$: '))
print(f'A metade de R${p} e R${moeda.metade(p)}')
print(f'O dobro de R${p} e R${moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p,10)}')
print(f'Diminuindo 10%, temos R${moeda.diminuir(p,10)}')

import module0

module0.run()