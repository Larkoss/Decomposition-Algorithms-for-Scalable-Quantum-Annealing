
from DBR import DBR
import networkx as nx
import random
from MVC_CQM import minimum_vertex_cover_cqm
import copy

def maximum_clique_exact_solve_np_hard(G_in):
	max_clique_number = nx.graph_clique_number(G_in)
	cliques = nx.find_cliques(G_in)
	for cl in cliques:
		if len(cl) == max_clique_number:
			return cl

def minimum_vertex_cover_exact_solve_np_hard(G):
	GC = nx.complement(G)
	nodes = list(G.nodes())
	MC = maximum_clique_exact_solve_np_hard(GC)
	return list(set(nodes)-set(MC))

for i in range(1):
    
    G = nx.gnp_random_graph(random.randint(66, 100), random.uniform(0.01, 0.99))
    G2 = copy.deepcopy(G)

    print("Original solution solution")
    print("Graph size: ", len(G), "\n")
    #soln = len(minimum_vertex_cover_exact_solve_np_hard(G2))
    solution_original = DBR(G, 20, minimum_vertex_cover_exact_solve_np_hard)
    #assert len(solution) == soln
    
    print("CQM solution")
    print("Graph size: ", len(G2), "\n")
    solution_cqm = DBR(G2, 20, minimum_vertex_cover_cqm)

    print("Original solution: ", solution_original)
    print("Length of Original solution: ", len(solution_original), "\n")
    print("CQM solution: ", solution_cqm)
    print("Length of exact solution: ", len(solution_cqm))
    #assert len(solution) == nx.graph_clique_number(G)