from graphviz import Digraph

g = Digraph('BucketSort', filename='bucket_fluxograma', format='png')
g.attr(rankdir='TB')

# Nós
g.node('A', 'Início')
g.node('B', 'Criar k baldes vazios')
g.node('C', 'Para cada elemento do vetor')
g.node('D', 'Calcular índice do balde')
g.node('E', 'Inserir elemento no balde correspondente')
g.node('F', 'Ordenar cada balde (Insertion Sort)')
g.node('G', 'Concatenar baldes em sequência')
g.node('H', 'Fim')

# Conexões
g.edge('A', 'B')
g.edge('B', 'C')
g.edge('C', 'D')
g.edge('D', 'E')
g.edge('E', 'C', label='Próximo elemento?', style='dashed')
g.edge('C', 'F')
g.edge('F', 'G')
g.edge('G', 'H')

# Gera o arquivo
g.render()
