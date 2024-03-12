#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetors

medida = float(input('Digite a medida (em m): '))

cm = medida*100
mm = medida*1000

print('O valor de {} m convertido e de {} cm e {} mm.'.format(medida, cm, mm))