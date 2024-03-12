# Crie um programa que leia duas notas de um aluno e calcule sua media mostrando uma mensagem no final de acordo com o valor:
# Media abaixo de 5, reprovado
# Media entre 5 e 6.9, recuperacao
# Media acima de 7, aprovado

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2)/2

if media < 5:
    print('Sua media foi de {}, voce esta REPROVADO!'.format(media))
elif 5 <= media <= 6.9:
    print('Sua media foi de {}, voce esta de RECUPERACAO!'.format(media))
else:
    print('Sua media foi de {}, voce esta APROVADO! PARABENS!'.format(media))