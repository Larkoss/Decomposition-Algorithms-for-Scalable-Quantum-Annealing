from DBK import DBK
from MC_CQM import maximum_clique_cqm
import networkx as nx
import random

def maximum_clique_exact_solve_np_hard(G):
	max_clique_number = nx.graph_clique_number(G)
	cliques = nx.find_cliques(G)
	for cl in cliques:
		if len(cl) == max_clique_number:
			return cl

for i in range(1):
    G = nx.gnp_random_graph(random.randint(66, 80), random.uniform(0.01, 0.99))
    
    print(len(G))
    print("Original solution solution\n")
    solution_original = DBK(G, 65, maximum_clique_exact_solve_np_hard)
    print("Original solution: ", solution_original)
    print("Length of solution: ", len(solution_original))
    #assert len(solution_original) == nx.graph_clique_number(G)
    
    print("CQM solution\n")
    solution_cqm = DBK(G, 65, maximum_clique_cqm)
    print("CQM solution: ", solution_cqm)
    print("Length of solution: ", len(solution_cqm))
    #assert len(solution) == nx.graph_clique_number(G)