import dimod
import networkx as nx
from dimod import ConstrainedQuadraticModel
from dimod import Binary
from dwave.system import DWaveSampler,AutoEmbeddingComposite
from itertools import combinations

def maximum_clique_cqm(G):

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
    return max_clique