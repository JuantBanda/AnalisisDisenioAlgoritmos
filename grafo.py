
class grafo:
    def __init__(self):
        self.nodos = set()
        self.aristas = dict()
        self.vecinos = dict()

    def agrega(self, x):
        self.nodos.add(x)
        if not x in self.vecinos:
            self.vecinos[x] = set()

    def conecta(self, x, y, peso):
        self.agrega(x)
        self.agrega(y)
        self.aristas[(x, y)] = peso
        self.vecinos[x].add(y)
        self.vecinos[y].add(x)

    #def camino(self,a,z):
    #    n2=self.nodos
    #    for x in range(5):
    #        n2.pop()
            #print(n2)
    #    return n2


G = grafo()
G.conecta('a', 'b', 1)
G.conecta('b', 'c', 2)
G.conecta('c', 'd', 3)
G.conecta('a', 'd', 4)
G.conecta('b', 'e', 8)
G.conecta('a', 'f', 7)
G.conecta('f', 'e', 6)
G.conecta('e', 'd', 5)
print("Nodos:",G.nodos)
print("Aristas con pesos:",G.aristas)
print("--------------------------------------------")
print("Vecinos de e:",G.vecinos['e'])
print("Vecinos de d:",G.vecinos['d'])
print("Grado de c:", len(G.vecinos['c']))
print("Grado de d:", len(G.vecinos['d']))
print("--------------------------------------------")

print("Hay un camino de 'a' a 'd'?")
#print(G.camino('a','d'))
