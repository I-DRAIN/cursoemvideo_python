''' Faca um programa que leia o sexo de uma pessoa, mas so aceite os valores 'M' ou 'F'. Caso esteja errado, peca a digitacao novamente ate ler um valor correto'''

correct = 0

while correct != 1:
    gender = str(input('Qual e o seu sexo: [M/F] ')).upper()
    
    if gender == 'M':
        correct += 1
        gender = 'Masculino'
    if gender == 'F':
        correct += 1
        gender = 'Feminino'
    if correct == 0:
        print('Sexo informado incorretamente.')

print('O Sexo digitado foi {}'.format(gender))