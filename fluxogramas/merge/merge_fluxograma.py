from graphviz import Digraph

g = Digraph('MergeSort', filename='merge_fluxograma', format='png')
g.attr(rankdir='TB')

g.node('A', 'Início')
g.node('B', 'Se tamanho da lista > 1')
g.node('C', 'Dividir lista em esquerda e direita')
g.node('D', 'MergeSort(esquerda)')
g.node('E', 'MergeSort(direita)')
g.node('F', 'Mesclar listas ordenadas')
g.node('G', 'Fim')

g.edge('A', 'B')
g.edge('B', 'C', label='Sim')
g.edge('B', 'G', label='Não')
g.edge('C', 'D')
g.edge('D', 'E')
g.edge('E', 'F')
g.edge('F', 'G')

g.render()
