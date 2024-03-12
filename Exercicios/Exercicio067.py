''' faca um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario.
O programa sera interrompido quando o numero solicitado for negativo'''

print('='*30)
print(' '*12+'TABUADA'+' '*11)
print('='*30)

n = int(input('Digite um numero: '))
while True:
    

    print('-'*30)
    for c in range(1,11):
        print(f'{n} X {c} = {n*c}')
    print('-'*30)

    n = int(input('Para continuar, digite outro numero: '))

    if n < 0:
        break

print('='*30)
print(f'Progama Finalizado!')
print('='*30)