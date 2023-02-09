import networkx as nx
import dimod
from dimod import ConstrainedQuadraticModel
from dimod import Binary
from itertools import combinations
from dwave.system import DWaveSampler,AutoEmbeddingComposite

G= nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)

G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(2,3)
G.add_edge(2,4)
G.add_edge(2,5)
G.add_edge(2,6)

print(G.nodes)
print(G.edges)

# x[i] = 1 if node[i] is in the maximum clique
# x[i] = 0 otherwise
x = {n: Binary(n) for n in G.nodes}

cqm = ConstrainedQuadraticModel()

# Set the objective to maximize the size of the clique
cqm.set_objective(-sum(x[i] for i in G.nodes))

# Add constraint that each node in the clique is connected to every other node in the clique
for i, j in combinations(G.nodes, 2):
    #ValueError: CQM must not have any quadratic constraints
    #if G.has_edge(i, j):
    #    cqm.add_constraint(x[i] + x[j] - 2 * x[i] * x[j] <= 1, label=f'{i}_{j}')
    if not G.has_edge(i,j):
        cqm.add_constraint(x[i] + x[j] <= 1, label = f'{i}_{j}')

bqm, invert = dimod.cqm_to_bqm(cqm)

sampler = DWaveSampler(api_key="DEV-75e04bc20be5cf5bc8a7d7924d08952738e2cefe")
embedding_sampler = AutoEmbeddingComposite(sampler)
sampleset = embedding_sampler.sample(bqm,num_reads = 100)

for smpl, energy in sampleset.data(['sample','energy']):
    max_clique = [n for n, value in smpl.items() if value == 1 and not str(n).startswith('slack')]
    mc_size = len(max_clique)
    break
print("=== Solver done ===") 
print(max_clique)