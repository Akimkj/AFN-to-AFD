#import os, platform
from graphviz import Digraph

'''def config_path_graphviz():
    if platform.system() == "Windows":
        path_bin = r"C:\Program Files\Graphviz\bin"

        if os.path.exists(path_bin):
            os.environ["PATH"] += os.pathsep + path_bin
'''

def visualizar_afd(afd):
    #config_path_graphviz()
    dot = Digraph(format="png")
    dot.attr(rankdir="LR", size="8,5")  # esquerda → direita

    # Estados
    for estado in afd["estados"]:

        if estado == "{}" or estado == "set()":
            continue
        
        if estado in afd["finais"]:
            dot.node(estado, shape="doublecircle")
        else:
            dot.node(estado, shape="circle")

    # Estado inicial
    dot.node("", shape="none")
    dot.edge("", afd["inicial"])

    # Transições
    transicoes = {}
    for (origem, simbolo), destino in afd["transicoes"].items():
        transicoes.setdefault((origem, destino), []).append(simbolo)

    for (origem, destino), simbolos in transicoes.items():
        rotulo = ",".join(simbolos)
        dot.edge(origem, destino, label=rotulo)


    dot.render("afd", directory="outputAFD", view=True)


