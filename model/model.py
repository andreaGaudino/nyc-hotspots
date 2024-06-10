import copy
import random

import networkx as nx

from database.DAO import DAO
from geopy.distance import distance


class Model:
    def __init__(self):
        self.providers = DAO.getAllProviders()
        self.graph = nx.Graph()


    def getCammino(self, target, substring):
        sources = self.getNodesMostVicini()
        source = sources[random.randint(0, len(sources)-1)][0]

        if not nx.has_path(self.graph, source, target):
            print(f"{source} e {target} non sono connessi")
            return [], source

        self.bestPath = []
        self.bestLen = 0
        parziale = [source]
        self.ricorsione(parziale, target, substring)

        return self.bestPath, source

    def ricorsione(self, parziale, target, substring):
        if parziale[-1] == target:
            if len(parziale) > self.bestLen:
                self.bestLen = len(parziale)
                self.bestPath = copy.deepcopy(parziale)

            return
        for v in self.graph.neighbors(parziale[-1]):
            if v not in parziale and substring not in v.loc:
                parziale.append(v)
                self.ricorsione(parziale, target, substring)
                parziale.pop()

    def getProviders(self):
        return self.providers

    def buildGraph(self, provider, soglia):
        self.graph.clear()
        #self.nodes = DAO.getLocationsOfProvider(provider)
        #self.graph.add_nodes_from(self.nodes)

        #add edges
        #modo 1 : faccio una query per gli archi
        # allEdges = DAO.getAllEdges(provider)
        # for edge in allEdges:
        #     l1 = edge[0]
        #     l2 = edge[1]
        #     if distance((l1.lat, l1.long), (l2.lat, l2.long)).km < soglia:
        #         self.graph.add_edge(l1.loc, l2.loc, weight = distance((l1.lat, l1.long), (l2.lat, l2.long)) )


        #modo 2 : modifico il metodo per i nodi e ci aggiungo le coordinate
        #dopo, doppio ciclo sui nodi e  mi calcolo la distanza su python

        self.nodes = DAO.getNodes2(provider)
        self.graph.add_nodes_from(self.nodes)
        for u in self.nodes:
            for v in self.nodes:
                if u!=v:
                    dist = distance((u.lat, u.long), (v.lat, v.long)).km
                    if dist<soglia:
                        self.graph.add_edge(u, v, weight=dist)




        #modo 3: doppio ciclo sui nodi e faccio una query ogni volta


    def getNodesMostVicini(self):
        listTuples = []
        for v in self.nodes:
            listTuples.append((v, len(list(self.graph.neighbors(v)))))
        listTuples.sort(key=lambda x: x[1], reverse=True)

        result = list(filter(lambda x: x[1] == listTuples[0][1], listTuples))
        return result





    def graphDetails(self):
        return len(self.graph.nodes), len(self.graph.edges)

    def getAllLocations(self):
        return list(self.graph.nodes)