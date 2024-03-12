""" Faca um programa que tenha uma funcao notas() que pode receber varias notas de alunos e vai retornar um dicionario com as seguintes informacoes:
    a) Quantidade de notas
    b) A maior nota
    c) A menor nota
    d) A media da turma
    e) A situacao (opcional)
    Adicione tambem as docstrings """
def notas(*n,sit=False):
    """
        -> funcao para analisar notas e situacoes de varios alunos/
        :param n: uma ou mais notas dos alunos (aceita varias)
        :param sit: valor pcional, indicando se deve ou nao adicionar a situacao
        :return: dicionario com varias informacoes sobre a situacao da turma 
    """
    r = dict()
    r["total"] = len(n)
    r["maior"] = max(n)
    r["menor"] = min(n)
    r["media"] = sum(n)/len(n)
    if sit:
        if r["media"] >= 7:
            r["situacao"] = 'BOA'
        elif r["media"] > 5:
            r["situacao"] = 'RAZOAVEL'
        else:
            r["situacao"] = 'RUIM'
    return r

#Programa Principal
resp = notas(5.5,2.5,10,6.5,8,sit=True)
print(resp)