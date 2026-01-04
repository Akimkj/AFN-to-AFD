#Função de validação do AFN de entrada
def validarAFN(afn):
    if (len(afn["estados"]) > 4):
        raise ValueError("[RESTRIÇÃO] - A quantidade máxima de estados é 4")
    if (len(afn["simbolos"]) > 3):
        raise ValueError("[RESTRIÇÃO] - A quantidade máxima de símbolos é 3")
    if (len(afn["transicoes"]) > 8):
        raise ValueError("[RESTRIÇÃO] - A quantidade máxima de transições é 8")

    erros = []

    #verifica se o estado inicial está entre os estados inseridos
    if afn["inicial"] not in afn["estados"]:
        erros.append(f"Estado inicial {afn["inicial"]} não está entre os estados")

    #verifica se os estados finais estão entre os estados inseridos
    for final in afn["finais"]:
        if final not in afn["estados"]:
            erros.append(f"Estado final {final} não está entre os estados")
    
    #verifica se cada transição não contém um estado de origem, de destino ou símbolo inválido (não informado)
    for (origem, simbolo), destinos in afn["transicoes"].items():
        if origem not in afn["estados"]:
            erros.append(f"Estado de origem {origem} não existe")
        if simbolo not in afn["simbolos"]:
            erros.append(f"Simbolo '{simbolo}' não existe")
        for destino in destinos:
            if destino not in afn["estados"]:
                erros.append(f"Estado de destino {destino} não existe")
    
    #caso haja algum erro, será disparado uma exceção e a execução será interrompida
    if erros:
        raise ValueError("AFN Inválido:\n" + "\n".join(erros))
    



#Função responsável por buscar os dados num arquivo .txt e criar o afn
def inputSearch(file):
    #abre o arquivo no modo de leitura
    with open(file, 'r', encoding='utf-8') as f:

        #definição da estrutura do afn
        afn = {
            "estados": set(),
            "simbolos": set(),
            "inicial": "",
            "finais": set(),
            "transicoes": {}
        }

        for line in f:
            line = line.strip()
            if not line:
                continue

            #separa a linha um vetor de strings para melhor manipulação   
            partes = line.split(" ")

            #leitura do estado inicial 
            if (line.startswith("inicial:")):
                afn["inicial"] = partes[-1].strip()
            
            #leitura de todos os simbolos do afn
            if (line.startswith("simbolos:")):
                alfabeto = partes[1:]
                for simbolos in alfabeto:
                    afn["simbolos"].add(simbolos)
            
            #leitura de todos os estados
            if (line.startswith("estados:")):
                estados = partes[1:]
                for estadoCur in estados:
                    afn["estados"].add(estadoCur)
            
            #leitura de todos os estados finais
            if (line.startswith("finais:")):
                estadosFinais = partes[1:]
                for estadoCur in estadosFinais:
                    afn["finais"].add(estadoCur)
            
            #leitura de todas as transições
            if (len(line.strip()) == 3):
                origem = line[0]
                simboloLeitura = line[1]
                destino = line[2]

                chave = (origem, simboloLeitura)

                if chave not in afn["transicoes"]:
                    afn["transicoes"][chave] = []

                if destino not in afn["transicoes"][chave]:
                    afn["transicoes"][chave].append(destino)

    #ordenação dos elementos do afn 
    afn["simbolos"] = sorted(afn["simbolos"])
    afn["estados"] = sorted(afn["estados"])
    afn["finais"] = sorted(afn["finais"])
    validarAFN(afn)
    return afn

