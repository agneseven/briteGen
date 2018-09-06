import networkx as nx
import matplotlib.pyplot as plt



class topoGeneration:
    #construct topology
    def __init__(self, nNodes, points_list, bandwidth_list, delay_list, coordinate_list):
        self.nNodes = nNodes
        self.points_list = points_list
        self.bandwidth_list = bandwidth_list
        self.delay_list = delay_list
        self.coordinate_list = coordinate_list


    def Graph(self):
        # upload the graph
        G=nx.Graph()
        G.add_edges_from(self.points_list)
        # add weights to edges
        for e in G.edges():
            G[e[0]][e[1]]['weight'] = self.bandwidth_list[e]
        G.add_nodes_from(self.coordinate_list.keys())
        #Just note that these positions won't be used as the position when drawing the graph, it has to be set explicitly.
        for n, p in self.coordinate_list.iteritems():
            G.node[n]['pos'] = p
        return G

    def showGraph(self):
    # show graph in a Figure
        G = self.Graph()
        pos = nx.spring_layout(G, 2, None,  self.coordinate_list)
        nx.draw_networkx_nodes(G,pos)
        nx.draw_networkx_edges(G,pos)
        nx.draw_networkx_labels(G,pos)
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        nx.draw_networkx(G, with_labels = True,pos=self.coordinate_list)

        plt.show()

    def adjMatrix(self):
        adjMatrix = nx.adjacency_matrix(G)
        print(adjMatrix.todense())

    def getDelayEdges(self, nodeA, nodeB):
        delay = self.delay_list(nodeA,nodeB)
        return delay


