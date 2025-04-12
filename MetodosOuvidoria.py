from opBD import *

def listaManifestacao(conn):
    consultaManifestacao = "select * from manifestacao"
    manifestacao = listarBancoDados(conn, consultaManifestacao)

    if not manifestacao:
        print("\nNenhuma manifestação encontrada!")
    else:
        print("\n == LISTA DEMANIFESTAÇÕES ==")
        for listaManifestacao in manifestacao:
            print(f"""
                id → {listaManifestacao[0]} 
                Tipo → {listaManifestacao[1]} 
                Descrição → {listaManifestacao[2]}
                """)

def listarTipoMani(conn):
    print("""== TIPOS ==  
    1 → Reclamação 
    2 → Elogio 
    3 → Sugestão""")
    try:
        opManifestacao = int(input("Informe o tipo: "))

        # Define o tipo correspondente à opção
        if opManifestacao == 1:
            tipo = "Reclamação"
        elif opManifestacao == 2:
            tipo = "Elogio"
        elif opManifestacao == 3:
            tipo = "Sugestão"
        else:
            print("Esta opção é inválida!\n")
            return

        # Consulta todas as manifestações do tipo selecionado
        consulta = "SELECT * FROM manifestacao WHERE tipo = %s"
        dados = (tipo,)
        manifestacoes = listarBancoDados(conn, consulta, dados)

        if not manifestacoes:
            print(f"\nAinda sem {tipo.lower()}!")
        else:
            print(f"\nTipo: {tipo}")
            for m in manifestacoes:
                print(f"Descrição: {m[2]}")  
            print() # Apenas para pular linha
    except ValueError:
        print("Digite apenas números inteiros!")

def criarMani(conn):
    print("""== TIPOS ==  
    1 → Reclamação 
    2 → Elogio  
    3 → Sugestão 
    4 → Sair""")

    try:
        opManifestacao = int(input("Informe o tipo: "))

        if opManifestacao == 4:
            print("Você decidiu parar de adicionar!")
            return

        if opManifestacao not in (1, 2, 3):
            print("Opção inválida! Digite 1, 2, 3 ou 4.")
            return

        # Define o tipo com base na opção
        tipo_manifestacao = {1: "Reclamação",2: "Elogio", 3: "Sugestão"}[opManifestacao]
        mani = input(f"Informe a(o) {tipo_manifestacao.lower()}: ").strip()

        if not mani:
            print("Descrição não pode ser vazia!")
            return

        consulta = 'INSERT INTO manifestacao (tipo, descricao) VALUES (%s, %s)'
        dadosManifestacao = (tipo_manifestacao, mani)
        codNovaMani = insertNoBancoDados(conn, consulta, dadosManifestacao)
        print(f"\nManifestação {codNovaMani} inserida com sucesso!")
        print() # Apenas para pular linha

    except ValueError:
        print("Erro: Digite apenas números inteiros.")

def obterQuantidadeManifestacoes(conn):
    consultaQuantidade = "SELECT COUNT(*) FROM manifestacao"
    resultado = listarBancoDados(conn, consultaQuantidade)

    if resultado:
        quantidadeManifestacoes = resultado[0][0]
        print(f"Atualmente temos {quantidadeManifestacoes} manifestações em nossa Ouvidoria.\n")
    else:
        print("Erro ao obter a quantidade de manifestações.")

def pesquisarManiCodigo(conn):
    try:
        codigoManifestacao = int((input("Digite o código da manifestação que deseja pesquisar: ")))

        consultaPesquisa = "select * from manifestacao where id = %s"
        dadosCodigo = (codigoManifestacao,)

        manifestacao = listarBancoDados(conn, consultaPesquisa, dadosCodigo)

        if not manifestacao:
            print("Nenhuma manifestação encontrada com esse código.")
        else:
            id_mani, tipo, descricao = manifestacao[0]
            print(f""" 
            == MANIFESTAÇÂO ENCONTRADA==
            ID: {id_mani}   
            Tipo: {tipo}
            Descrição: {descricao}
            """)
    except ValueError:
        print("Erro: Digite apenas números inteiros!")

def ExcluirPeloCodigo(conn):
        try:
            codigoRemocao = int(input("Digite o código da manifestação que deseja remover: "))

            consultaRemocao = 'delete from manifestacao where id = %s'
            dados = (codigoRemocao,)

            linhasAfetadas = excluirBancoDados(conn,consultaRemocao,dados)

            if linhasAfetadas > 0:
                print("Manifestação excluida com sucesso!")

            else:
                print("Nenhuma manifestação encontrada com esse código.")
        except ValueError:
            print("Erro: Digite apenas números para o código.")