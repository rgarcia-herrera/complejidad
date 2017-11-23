import networkx as nx  # uso networkx para poder usar red.neighbors(nodo)
import random
import matplotlib.pyplot as plt  # para plotear mapas


class Patch:
    """
    una celda
    """

    def __init__(self, pheno=0):
        self.pheno = pheno

    def diferenciar(self, inner_neighbors, outer_neighbors, w=0.4):
        """
        elige entre D y U
        """
        AD = 0
        for p in inner_neighbors:
            if p.pheno == 1:
                AD += 1

        ID = 0
        for p in outer_neighbors:
            if p.pheno == 1:
                ID += 1

        x = AD - w * ID

        if x > 0:
            self.pheno = 1
        elif x < 0:
            self.pheno = 0

    def __repr__(self):
        return u"%s" % self.pheno


class Universe:

    def __init__(self, width=20, height=20):
        self.height = width
        self.width = height

        self.grid = [[Patch() for i in range(width)]
                     for j in range(height)]

        self.g = nx.Graph()
        self.connect_moore()

    def outer_neighbors(self, p):
        o = set()
        for n in self.g.neighbors(p):
            o.add(n)
            for m in self.g.neighbors(n):
                o.add(m)
                for k in self.g.neighbors(m):
                    o.add(k)
                    for j in self.g.neighbors(k):
                        if j != p:
                            o.add(j)
        return o

    def inner_neighbors(self, p):
        o = set()
        for n in self.g.neighbors(p):
            o.add(n)
            for m in self.g.neighbors(p):
                o.add(n)
                for nn in self.g.neighbors(m):
                    if nn != p:
                        o.add(nn)
        return o

    def connect_moore(self):
        """ conecta nodos de la reticula para crear vecindarios de Moore """
        for x in range(self.width):
            for y in range(self.height):
                # cada patch
                patch = self.grid[x][y]
                # connecta a vecindario
                for i in [x-1, x, x+1 if x+1 < self.width else -1]:
                    for j in [y-1, y, y+1 if y+1 < self.height else -1]:
                        self.g.add_edge(patch, self.grid[i][j])

        # quitamos autoconexiones
        self.g.remove_edges_from(self.g.selfloop_edges())

    def randomiza_phenotipo(self):
        for p in self.g.nodes():
            p.pheno = random.choice([0, 1])

    def plot(self, path):
        """
        grafica mapa de calor del grid
        """
        mapa = [[self.grid[i][j].pheno for i in range(self.width)]
                for j in range(self.height)]

        plt.imshow(mapa,
                   cmap='tab10',
                   interpolation='nearest')
        plt.savefig(path)
        plt.cla()
