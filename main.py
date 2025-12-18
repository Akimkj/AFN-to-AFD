from src.conversor_afd import afn_to_afd
from src.tabela import imprimir_tabela_afd
from src.visualizacao import visualizar_afd

afn_teste = {
    "estados": ["A", "B", "C", "D"],
    "simbolos": ["0", "1"],
    "inicial": "A",
    "finais": ["D"],
    "transicoes": {
        ("A", "0"): "B",
        ("A", "1"): "A",
        ("A", "0"): "A",
        ("B", "0"): "C",
        ("B", "1"): "B",
        ("C", "0"): "D",
        ("C", "1"): "C",
        ("D", "0"): "D",
        ("D", "1"): "D"
    }
}

afd_teste = afn_to_afd(afn_teste)
imprimir_tabela_afd(afd_teste)


visualizar_afd(afd_teste)



