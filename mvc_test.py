import networkx as nx
import dimod
from dimod import ConstrainedQuadraticModel
from dimod import Binary
from itertools import combinations
import math

g= nx.Graph()
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_node(5)
g.add_node(6)

g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(2,4)
g.add_edge(2,5)
g.add_edge(2,6)

print(g.nodes)
print(g.edges)

# x[i] = 1 if node[i] is in minimum vertex cover
# x[i] = 0 otherwise
x = {n: Binary(n) for n in g.nodes}

cqm = ConstrainedQuadraticModel()

# Set the objective to minimize the size of the cover
cqm.set_objective(sum(x[i] for i in g.nodes))

# Add constraint that each edge has at least a node in the cover
for (i,j) in g.edges:
    cqm.add_constraint(x[i] + x[j] >= 1, label = f'edge{i}_{j}')
        
bqm, invert = dimod.cqm_to_bqm(cqm)

from dwave.system import DWaveSampler,AutoEmbeddingComposite
sampler = DWaveSampler(DWAVE_API_TOKEN="DEV-75e04bc20be5cf5bc8a7d7924d08952738e2cefe")
embedding_sampler = AutoEmbeddingComposite(sampler)
sampleset = embedding_sampler.sample(bqm,num_reads = 100)


for smpl, energy in sampleset.data(['sample','energy']):
    print(sampleset.data(['sample','energy']))
    minimum_vertex_cover = [n for n, value in smpl.items() if value == 1 and not str(n).startswith('slack')]
    mvc_size = len(minimum_vertex_cover)
    break
print(minimum_vertex_cover)
print("SOLVER DONE") 

