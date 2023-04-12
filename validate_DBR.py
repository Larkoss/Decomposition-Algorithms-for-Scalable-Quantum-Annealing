
from DBR import DBR
import networkx as nx
from MVC_chimera import minimum_vertex_cover_chimera
from MVC_pegasus import minimum_vertex_cover_pegasus
import copy
import time
import jgrapht
from jgrapht import create_graph
import matplotlib.pyplot as plt

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
for i in range(1): #20 - 125
    for j in range(3): #0.1 - 0.9
        num_nodes = 80 + i * 5
        num_density = 0.1 + j * 0.1
        G = nx.gnp_random_graph(num_nodes, num_density) 
        pos = nx.spring_layout(G)  # compute the node positions
        for x in range(3): #10-25
            f = open("test.txt", "a")

            print(G)

            num_limit = 10 + x * 5
            G1 = copy.deepcopy(G) 
            G2 = copy.deepcopy(G)
            G3 = copy.deepcopy(G)
            G4 = create_graph(directed=False, weighted=False)
            for v in G.nodes():
                G4.add_vertex(v)
            for u, v in G.edges():
                G4.add_edge(u, v)

            plt.clf()
            print("\njgrapht solution")
            print("Graph size: ", len(G), "\n")
            start = time.time()
            solution_jgrapht = jgrapht.algorithms.vertexcover.exact(G4)
            solution_jgrapht = solution_jgrapht[1]
            end = time.time()
            time_jgrapht = end - start
            
            
            nx.draw_networkx_nodes(G, pos, nodelist=solution_jgrapht, node_color='blue')
            nx.draw_networkx_nodes(G, pos, nodelist=set(G.nodes()) - set(solution_jgrapht), node_color='grey')
            nx.draw_networkx_edges(G, pos)  # draw the edges
            nx.draw_networkx_labels(G, pos)  # add the node labels
            plt.savefig('Nodes' + str(num_nodes) + 'density' + str(int(num_density * 10)) + 'limit' + str(num_limit) + 'jgrapht.png', dpi=300, bbox_inches='tight')

            plt.clf()
            print("Original solution's solution")
            print("Graph size: ", len(G1))
            #soln = len(minimum_vertex_cover_exact_solve_np_hard(G2))
            start = time.time()
            solution_original = DBR(G1, num_limit, minimum_vertex_cover_exact_solve_np_hard)
            end = time.time()
            time_original = end - start
            #assert len(solution) == soln
            nx.draw_networkx_nodes(G, pos, nodelist=solution_original, node_color='red')
            nx.draw_networkx_nodes(G, pos, nodelist=set(G.nodes()) - set(solution_original), node_color='grey')
            nx.draw_networkx_edges(G, pos)  # draw the edges
            nx.draw_networkx_labels(G, pos)  # add the node labels
            plt.savefig('Nodes' + str(num_nodes) + 'density' + str(int(num_density * 10)) + 'limit' + str(num_limit) + 'original.png', dpi=300, bbox_inches='tight')
            
            plt.clf()
            print("\nPegasus solution")
            print("Graph size: ", len(G2))
            start = time.time()
            solution_pegasus = DBR(G2, num_limit, minimum_vertex_cover_pegasus)
            end = time.time()
            time_pegasus = end - start
            nx.draw_networkx_nodes(G, pos, nodelist=solution_pegasus, node_color='green')
            nx.draw_networkx_nodes(G, pos, nodelist=set(G.nodes()) - set(solution_pegasus), node_color='grey')
            nx.draw_networkx_edges(G, pos)  # draw the edges
            nx.draw_networkx_labels(G, pos)  # add the node labels
            plt.savefig('Nodes' + str(num_nodes) + 'density' + str(int(num_density * 10)) + 'limit' + str(num_limit) + 'pegasus.png', dpi=300, bbox_inches='tight')

            plt.clf()
            print("\nChimera solution")
            print("Graph size: ", len(G3))
            start = time.time()
            solution_chimera = DBR(G3, num_limit, minimum_vertex_cover_chimera)
            end = time.time()
            time_chimera = end - start
            nx.draw_networkx_nodes(G, pos, nodelist=solution_chimera, node_color='yellow')
            nx.draw_networkx_nodes(G, pos, nodelist=set(G.nodes()) - set(solution_chimera), node_color='grey')
            nx.draw_networkx_edges(G, pos)  # draw the edges
            nx.draw_networkx_labels(G, pos)  # add the node labels
            plt.savefig('Nodes' + str(num_nodes) + 'density' + str(int(num_density * 10)) + 'limit' + str(num_limit) + 'chimera.png', dpi=300, bbox_inches='tight')

            print("Original jgrapht: ", solution_jgrapht)
            print("Length of jgrapht solution: ", len(solution_jgrapht), "\n")
            print("Original solution: ", solution_original)
            print("Length of Original solution: ", len(solution_original), "\n")
            print("Pegasus solution: ", solution_pegasus)
            print("Length of pegasus solution: ", len(solution_pegasus),"\n")
            print("Chimera solution: ", solution_chimera)
            print("Length of chimera solution: ", len(solution_chimera),"\n")
            #assert len(solution) == nx.graph_clique_number(G)
            f.write("len jgrapht: " + str(len(solution_jgrapht)) + " len Ori: " + str(len(solution_original)) + " len pegasus: " + str(len(solution_pegasus)) + " len chimera: " + str(len(solution_chimera)))
            f.write(" Time jgrapht: " + str(time_jgrapht) + " Time Ori: " + str(time_original) + " Time pegasus: " + str(time_pegasus) + " Time chimera: " + str(time_chimera))
            f.write(" Limit: " + str(10) + "\n")           
            #assert len(solution_pegasus) == len(solution_original)
            f.close()

