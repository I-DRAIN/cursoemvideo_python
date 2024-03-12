# Desenvolva uma logica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com:
# Abaixo de 18.5: Abaixo do peso. Entre 18.5 e 25: Peso ideal. 25 e 30: sobrepeso. 30 a 40, Obesidade. Acima de 40, Morbida.

peso = float(input('Qual e seu peso: '))
altura = float(input('Qual e sua altura: '))

IMC = peso/(altura**2)

print('Seu IMC e {}!'.format(IMC))
if IMC <= 18.5:
    print('Abaixo do Peso!')
elif IMC <= 25:
    print('Peso Ideal!')
elif IMC <= 30:
    print('Sobrepeso!')
elif IMC <= 40:
    print('Obesidade!')
else:
    print('Obesidade Morbida!')