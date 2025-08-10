from graphviz import Digraph

# Cria o gráfico
g = Digraph('BubbleSort', filename='bubble_fluxograma', format='png')
g.attr(rankdir='TB')  # Direção: Top to Bottom (cima pra baixo)

# Define os nós
g.node('A', 'Início')
g.node('B', 'Para i de 0 até n-1')
g.node('C', 'Para j de 0 até n-i-1')
g.node('D', 'Se A[j] > A[j+1]')
g.node('E', 'Trocar A[j] e A[j+1]')
g.node('F', 'Fim')

# Define as conexões (arestas)
g.edge('A', 'B')
g.edge('B', 'C')
g.edge('C', 'D')
g.edge('D', 'E', label='Sim')
g.edge('D', 'C', label='Não', style='dashed')
g.edge('E', 'C')
g.edge('C', 'F')

# Gera a imagem
g.render()
