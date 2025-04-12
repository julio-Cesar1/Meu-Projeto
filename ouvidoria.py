from opBD import *
from ouvidoria_copy import *

opcao = 0
conn = criarConexao('localhost', 'root', 'Julio132@', 'ouvidoria')

while opcao != 7:
    print("""== MENU DO SISTEMA ==
    1)Listagem das Manifestação 
    2)Listagem de Manifestação por Tipo 
    3)Criar uma Nova Manifestação 
    4)Exibir Quantidade de Manifestação 
    5)Pesquisar uma Manifestação por Código 
    6)Excluir uma Manifestação pelo Código 
    7)Sair do Sistema""")
    try: 
        opcao = int(input("\nDigite a opção: "))
        if opcao == 1:
            listaManifestacao(conn)

        elif opcao == 2:
            listarTipoMani(conn)

        elif opcao == 3:
            criarMani(conn)

        elif opcao == 4:
            obterQuantidadeManifestacoes(conn)

        elif opcao == 5:
            pesquisarManiCodigo(conn)

        elif opcao == 6:
            ExcluirPeloCodigo(conn)

        elif opcao == 7:
            print("Obrigado(a) por utilizar a nossa Ouvidoria!")
            break
    except ValueError:
        print("Digite apenas numeros inteiros!")

encerrarConexao(conn)