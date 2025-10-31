from graphviz import Digraph

g = Digraph('SmoothSort', filename='smooth_fluxograma', format='png')
g.attr(rankdir='TB')

# Nós
g.node('A', 'Início')
g.node('B', 'Construir sequência de heaps de Leonardo')
g.node('C', 'Para i de n-1 até 1')
g.node('D', 'Trocar A[0] com A[i]')
g.node('E', 'Reduzir tamanho do heap')
g.node('F', 'Restaurar propriedade de heap de Leonardo')
g.node('G', 'Mais elementos a ordenar?')
g.node('H', 'Fim')

# Conexões
g.edge('A', 'B')
g.edge('B', 'C')
g.edge('C', 'D')
g.edge('D', 'E')
g.edge('E', 'F')
g.edge('F', 'G')
g.edge('G', 'C', label='Sim')
g.edge('G', 'H', label='Não', style='dashed')

# Gera o arquivo
g.render()
