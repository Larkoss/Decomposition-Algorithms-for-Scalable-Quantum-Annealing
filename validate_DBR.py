
from DBR import DBR
import networkx as nx
from MVC_CQM import minimum_vertex_cover_cqm
import copy
import time

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

f = open("results-test.txt", "w")

for i in range(7):
    
    G = nx.gnp_random_graph(i * 5 + 10, 0.2)
    G2 = copy.deepcopy(G)

    print("Original solution solution")
    print("Graph size: ", len(G), "\n")
    #soln = len(minimum_vertex_cover_exact_solve_np_hard(G2))
    start = time.time()
    solution_original = DBR(G, 20, minimum_vertex_cover_exact_solve_np_hard)
    end = time.time()
    time_original = end - start
    #assert len(solution) == soln
    
    print("CQM solution")
    print("Graph size: ", len(G2), "\n")
    start = time.time()
    solution_cqm = DBR(G2, 20, minimum_vertex_cover_cqm)
    end = time.time()
    time_cqm = end - start

    print("Original solution: ", solution_original)
    print("Length of Original solution: ", len(solution_original), "\n")
    print("CQM solution: ", solution_cqm)
    print("Length of cqm solution: ", len(solution_cqm),"\n")
    #assert len(solution) == nx.graph_clique_number(G)
    f.write("len Ori: " + str(len(solution_original)) + " len CQM: " + str(len(solution_cqm)))
    f.write(" Time Ori: " + str(time_original) + " Time CQM: " + str(time_cqm) + "\n")
    #assert len(solution_cqm) == len(solution_original)
f.close()
