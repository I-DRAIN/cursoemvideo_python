from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair'])
    if resposta == 1:
        # Opcao de listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Opcao de cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Ate logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opcao valida\033[m')
    sleep(2)