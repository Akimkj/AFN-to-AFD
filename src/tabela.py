def imprimir_tabela_afd(afd):
    estados = afd["estados"]  # lista de estados do AFD (já em formato de string)
    simbolos = list(afd["simbolos"])  # lista de símbolos do alfabeto do AFD
    transicoes = afd["transicoes"]  # dicionário de transições do AFD: (estado, símbolo) -> destino

    # largura fixa para formatar cada coluna na tabela
    largura = 15   

    # cria o cabeçalho da tabela: primeiro "Estado", depois cada símbolo
    cabecalho = ["Função programa"] + simbolos 

    # monta a linha do cabeçalho já centralizada
    linha_cabecalho = " | ".join(h.ljust(largura) for h in cabecalho)

    print(linha_cabecalho)  # mostra o cabeçalho na tela
    print("-" * len(linha_cabecalho))  # linha de separação abaixo do título

    # para cada estado do AFD, imprime sua linha da tabela
    for estado in estados:
        # começa a linha com o nome do estado
        linha = estado.ljust(largura)

        # para cada símbolo, pega o destino da transição
        for simbolo in simbolos:

            # pega o destino correspondente ao par (estado, símbolo), se não existir a transição, retorna "{}"
            destino = transicoes.get((estado, simbolo), "{}")

            # adiciona o destino formatado na linha
            linha += " | " + destino.ljust(largura)

        # imprime a linha completa do estado    
        print(linha)