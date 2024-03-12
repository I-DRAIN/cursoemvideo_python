""" Crie um programa que tenha uma funcao fatorial() que receba dois parametros: o primeiro que indique o numero a calcular e o outro chamado show, que 
sera um valor logico (opcional) indicando se sera mostrado ou nao na tela o processo de calculo do fatorial"""

def fatorial(n, show=False):
    """
        -> Calula o Fatorial de um numero.
        : param n: O numero a ser calculado.
        : param show: (opcional) Mostrar ou nao a conta.
        : return: O valor do Fatorial de um numero n.
    """
    f = 1
    for i in range (n,0,-1):
        if show:
            if i == 1:
                print(f'{i} = ', end = '')
            else:
                print(f'{i} x ',end ='')
        f *= i
    return f


            


# Programa principal 
print(fatorial(5))
