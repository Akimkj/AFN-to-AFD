def inputSearch(file):
    with open(file, 'r', encoding='utf-8') as f:

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

            partes = line.split(" ")

            if (line.startswith("inicial:")):
                afn["inicial"] = partes[-1].strip()
            
            if (line.startswith("simbolos:")):
                alfabeto = partes[1:]
                for simbolos in alfabeto:
                    afn["simbolos"].add(simbolos)
            
            if (line.startswith("estados:")):
                estados = partes[1:]
                for estadoCur in estados:
                    afn["estados"].add(estadoCur)
                
            if (line.startswith("finais:")):
                estadosFinais = partes[1:]
                for estadoCur in estadosFinais:
                    afn["finais"].add(estadoCur)
            
            if (len(line.strip()) == 3):
                origem = line[0]
                simboloLeitura = line[1]
                destino = line[2]

                chave = (origem, simboloLeitura)

                if chave not in afn["transicoes"]:
                    afn["transicoes"][chave] = []

                if destino not in afn["transicoes"][chave]:
                    afn["transicoes"][chave].append(destino)

    afn["simbolos"] = sorted(afn["simbolos"])
    afn["estados"] = sorted(afn["estados"])
    afn["finais"] = sorted(afn["finais"])
    return afn

