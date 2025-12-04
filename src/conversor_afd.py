from collections import deque


from collections import deque

def mover(afn, conjunto, simbolo):
    resultado = set()

    for estado in conjunto:
        chave = (estado, simbolo)
        if chave in afn["transicoes"]:
            resultado.update(afn["transicoes"][chave])
    
    return resultado


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
def converter_afn_para_afd(afn):

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
            destino = frozenset(mover(afn, atual, simb))

            afdTransicoes[(atual, simb)] = destino

            #Verificação se o novo conjunto não está entre os visitados
            if destino not in visitados:
                visitados.add(destino)
                fila.append(destino)
                afdEstados.add(destino)



    # ----- Definir Estados Finais do AFD ------
    afnFinais = set(["finais"])

    for conjunto in afdEstados:
        #Verifica se para conjunto nos estados do AFD, há interseção com os estados finais do AFN
        if len(conjunto & afnFinais) > 0:
            afdFinais.add(conjunto)
    






