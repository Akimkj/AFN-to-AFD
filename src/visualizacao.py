import os

os.environ["PATH"] += os.pathsep + r"C:\Program Files\Graphviz\bin"

from graphviz import Digraph


def visualizar_afd(afd):
    dot = Digraph(format="png")
    dot.attr(rankdir="LR")  # esquerda → direita

    # Estados
    for estado in afd["estados"]:
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

    dot.view()


