from graphviz import Digraph

g = Digraph('SelectionSort', filename='selection_fluxograma', format='png')
g.attr(rankdir='TB')

g.node('A', 'Início')
g.node('B', 'Para i de 0 até n-2')
g.node('C', 'min_idx = i')
g.node('D', 'Para j de i+1 até n-1')
g.node('E', 'Se A[j] < A[min_idx]')
g.node('F', 'min_idx = j')
g.node('G', 'Trocar A[i] com A[min_idx]')
g.node('H', 'Fim')

g.edge('A', 'B')
g.edge('B', 'C')
g.edge('C', 'D')
g.edge('D', 'E')
g.edge('E', 'F', label='Sim')
g.edge('F', 'D')
g.edge('E', 'D', label='Não', style='dashed')
g.edge('D', 'G')
g.edge('G', 'B')
g.edge('B', 'H')

g.render()
