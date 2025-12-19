from collections import deque


'''
Esta função retorna um novo conjunto contendo o estado destino quando o estado atual ler tal símbolo.

No AFD, cada estado é representado por um subconjunto de estados do AFN.
'''
def trasition(afn, conjunto, simbolo):
    resultado = set()

    #Itera sobre cada estado presente no conjunto atual
    for estado in conjunto:
        chave = (estado, simbolo)
        
        #se existir essa transação em afn, adicionamos todos os destinos no resultado
        if chave in afn["transicoes"]:
            resultado.update(afn["transicoes"][chave]) 
    
    return resultado

#Conversão dos dados em string
def set_to_string(s):
    if len(s) == 0:
        return "{}"
    return "".join(sorted(s))


"""
    Recebe um AFN no formato:

        afn = {
            "estados": ["0", "1", "2"],
            "simbolos": ["a", "b"],
            "inicial": "0",
            "finais": ["2"],
            "transicoes": {
                ("0","a"): ["1","2"],
                ("1","b"): ["2"]
            }
        }

    Retorna um AFD no formato:

        afd = {
            "estados": [...],
            "simbolos": [...],
            "inicial": "0",
            "finais": [...],
            "transicoes": { (orig, simb): dest }
        }
"""
def afn_to_afd(afn):

    # ----- Estado Inicial do AFD ------ 
    inicial = frozenset([afn["inicial"]])


    fila = deque([inicial])
    visitados = set([inicial])

    #Conjuntos e objetos que serão usados para formar o AFD
    afdTransicoes = {}
    afdEstados = set([inicial]) 
    afdFinais = set()

    #------ Subset Construction --------
    while (fila):
        #Pega o estado atual do AFN
        atual = fila.popleft()

        #Para cada símbolo do alfabeto, é analisado qual o próximo estado, e assim se formam as transições
        for simb in afn["simbolos"]:
            #Uso de frozenset para analisar se o novo conjunto (destino) está dentro do conjunto principal (visitados)
            destino = frozenset(trasition(afn, atual, simb))

            # Se destino é vazio, NÃO adiciona como estado do AFD
            if len(destino) == 0:
                continue

            afdTransicoes[(atual, simb)] = destino

            #Verificação se o novo conjunto não está entre os visitados
            if destino not in visitados:
                visitados.add(destino)
                fila.append(destino)
                afdEstados.add(destino)



    # ----- Definir Estados Finais do AFD ------
    afnFinais = set(afn["finais"])

    for conjunto in afdEstados:
        #Verifica se para conjunto nos estados do AFD, há interseção com os estados finais do AFN
        if len(conjunto & afnFinais) > 0:
            afdFinais.add(conjunto)
    
    #Criação do objeto AFD
    afd = {
        "estados": sorted([set_to_string(s) for s in afdEstados]),
        "simbolos": afn["simbolos"],
        "inicial": set_to_string(inicial),
        "finais": sorted([set_to_string(s) for s in afdFinais]),
        "transicoes": {}
    }

    #Converter chaves e valores das transições
    for (origem_set, simb), destino_set in afdTransicoes.items():
        origem = set_to_string(origem_set)
        destino = set_to_string(destino_set)
        afd["transicoes"][(origem, simb)] = destino
    
    return afd







