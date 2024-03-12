# Faca um algortimo que leia o salario de um funcionario e 
# mostre seu novo salario com 15% de aumento

salario = float(input('Digite o salario: '))

aumento = salario*0.15
novosalario = salario + aumento

print('Originalmente, o salario era de {}. Com o aumento de 15% o novo salario e de {}.'
.format(salario, novosalario))