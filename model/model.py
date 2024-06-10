import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.providers = DAO.getAllProviders()
        self.graph = nx.Graph()

    def getProviders(self):
        return self.providers

    def buildGraph(self, provider):
        self.nodes = DAO.getLocationsOfProvider(provider)
        self.graph.add_nodes_from(self.nodes)

        #add edges
        #modo 1 : faccio una query per gli archi
        allEdges = DAO.getAllEdges(provider)
        o =0


        #modo 2 : modifico il metodo per i nodi e ci aggiungo le coordinate
        #dopo, doppio ciclo sui nodi e  mi calcolo la distanza su python




        #modo 3: doppio ciclo sui nodi e faccio una query ogni volta

    def graphDetails(self):
        return len(self.graph.nodes), len(self.graph.edges)