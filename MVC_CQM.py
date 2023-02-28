import dimod
import networkx as nx
from dimod import ConstrainedQuadraticModel
from dimod import Binary
from dwave.system import DWaveSampler,AutoEmbeddingComposite
from itertools import combinations
#import dwave.inspector

def minimum_vertex_cover_cqm(G):

    # x[i] = 1 if node[i] is in minimum vertex cover
    # x[i] = 0 otherwise
    x = {n: Binary(n) for n in G.nodes}

    cqm = ConstrainedQuadraticModel()

    # Set the objective to minimize the size of the cover
    cqm.set_objective(sum(x[i] for i in G.nodes))

    # Add constraint that each edge has at least a node in the cover
    for (i,j) in G.edges:
        cqm.add_constraint(x[i] + x[j] >= 1, label = f'edge{i}_{j}')
            
    bqm, invert = dimod.cqm_to_bqm(cqm)
    
    #sampler = DWaveSampler()
    sampler = DWaveSampler(solver={'topology__type': 'chimera'})
    embedding_sampler = AutoEmbeddingComposite(sampler)
    sampleset = embedding_sampler.sample(bqm,num_reads = 100)

    #dwave.inspector.show(sampleset)


    for smpl, energy in sampleset.data(['sample','energy']):
        minimum_vertex_cover = [n for n, value in smpl.items() if value == 1 and not str(n).startswith('slack')]
        mvc_size = len(minimum_vertex_cover)
        break
    
    print("=== DWave done ===") 
    return minimum_vertex_cover