from src.conversor_afd import afn_to_afd
from src.tabela import imprimir_tabela_afd
from src.visualizacao import visualizar_afd
from src.inputBusca import inputSearch


afn = inputSearch('inputAFN.txt')
afd = afn_to_afd(afn)
imprimir_tabela_afd(afd)
visualizar_afd(afd)




