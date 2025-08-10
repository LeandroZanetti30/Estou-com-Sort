from graphviz import Digraph

g = Digraph('QuickSort', filename='quick_fluxograma', format='png')
g.attr(rankdir='TB')

g.node('A', 'Início')
g.node('B', 'Se início < fim')
g.node('C', 'p = partição(A, início, fim)')
g.node('D', 'QuickSort(A, início, p-1)')
g.node('E', 'QuickSort(A, p+1, fim)')
g.node('F', 'Fim')

g.edge('A', 'B')
g.edge('B', 'C', label='Sim')
g.edge('B', 'F', label='Não')
g.edge('C', 'D')
g.edge('D', 'E')
g.edge('E', 'F')

g.render()
