
from DBR import DBR
import networkx as nx
from MVC_chimera import minimum_vertex_cover_chimera
from MVC_pegasus import minimum_vertex_cover_pegasus
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

#f = open("test.txt", "a")
for i in range(5): #10 - 125
    for j in range(9): #0.1 - 0.9
        f = open("test.txt", "a")
        G = nx.gnp_random_graph(80 + i * 5, 0.1 + j * 0.1) 
        G2 = copy.deepcopy(G)
        G3 = copy.deepcopy(G)

        print("Original solution solution")
        print("Graph size: ", len(G), "\n")
        #soln = len(minimum_vertex_cover_exact_solve_np_hard(G2))
        start = time.time()
        solution_original = DBR(G, 10, minimum_vertex_cover_exact_solve_np_hard)
        end = time.time()
        time_original = end - start
        #assert len(solution) == soln
        
        print("Pegasus solution")
        print("Graph size: ", len(G2), "\n")
        start = time.time()
        solution_pegasus = DBR(G2, 10, minimum_vertex_cover_pegasus)
        end = time.time()
        time_pegasus = end - start

        print("Chimera solution")
        print("Graph size: ", len(G3), "\n")
        start = time.time()
        solution_chimera = DBR(G3, 10, minimum_vertex_cover_chimera)
        end = time.time()
        time_chimera = end - start

        print("Original solution: ", solution_original)
        print("Length of Original solution: ", len(solution_original), "\n")
        print("Pegasus solution: ", solution_pegasus)
        print("Length of pegasus solution: ", len(solution_pegasus),"\n")
        print("Chimera solution: ", solution_chimera)
        print("Length of chimera solution: ", len(solution_chimera),"\n")
        #assert len(solution) == nx.graph_clique_number(G)
        f.write("len Ori: " + str(len(solution_original)) + " len pegasus: " + str(len(solution_pegasus)) + " len chimera: " + str(len(solution_chimera)))
        f.write(" Time Ori: " + str(time_original) + " Time pegasus: " + str(time_pegasus) + " Time chimera: " + str(time_chimera))
        f.write(" Limit: " + str(10) + "\n")           
        #assert len(solution_pegasus) == len(solution_original)
        f.close()

