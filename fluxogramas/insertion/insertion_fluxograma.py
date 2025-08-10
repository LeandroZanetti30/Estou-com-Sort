from graphviz import Digraph

g = Digraph('InsertionSort', filename='insertion_fluxograma', format='png')
g.attr(rankdir='TB')

g.node('A', 'Início')
g.node('B', 'Para i de 1 até n-1')
g.node('C', 'Chave = A[i]')
g.node('D', 'j = i - 1')
g.node('E', 'Enquanto j >= 0 e A[j] > chave')
g.node('F', 'A[j+1] = A[j]')
g.node('G', 'j = j - 1')
g.node('H', 'A[j+1] = chave')
g.node('I', 'Fim')

g.edge('A', 'B')
g.edge('B', 'C')
g.edge('C', 'D')
g.edge('D', 'E')
g.edge('E', 'F', label='Sim')
g.edge('F', 'G')
g.edge('G', 'E')
g.edge('E', 'H', label='Não')
g.edge('H', 'B')
g.edge('B', 'I')

g.render()
