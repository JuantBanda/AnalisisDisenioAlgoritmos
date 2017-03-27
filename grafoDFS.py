
class grafo:
    def __init__(self):
        self.nodos = set()
        self.aristas = dict()
        self.vecinos = dict()
        self.salidas=dict()

    def agrega(self, x):
        self.nodos.add(x)
        if not x in self.vecinos:
            self.vecinos[x] = set()
            self.salidas[x] = list()

    def conecta(self, x, y, peso):
        self.agrega(x)
        self.agrega(y)
        self.aristas[(x, y)] = peso
        self.vecinos[x].add(y)
        self.vecinos[y].add(x)
        self.salidas[x].append(y)

    def camino(self,inicio,final):
        base=inicio
        checados=set()
        candidatos=set()
        checados.add(base)
        candidatos.add(base)
        while(True):
            if len(candidatos)==0:
                return False
                break
            base=candidatos.pop()
            for j in range(len(self.salidas[base])):
                punt=self.salidas[base][j]
                if punt==final:
                    return True
                if punt not in checados:
                    candidatos.add(punt)

    def DFS(self, inicio):
        pila=list()
        visitados=set()
        pila.append(inicio)
        visitados.add(inicio)
        base=inicio
        while(len(pila)!=0):
            print(pila)
            cont=0
            for j in self.vecinos[base]:
                if j not in visitados:
                    visitados.add(j)
                    pila.append(j)
                    break
                else:
                    cont+=1
            if cont==len(self.vecinos[base]):
                pila.pop()
            if len(pila)!=0:
                base=pila[-1]


G = grafo()
archivo=open("instancia_grafo.txt", "r")
for linea in archivo.readlines():
    dato=linea.split("\n")[0]
    dato=dato.split(" ")
    G.conecta(dato[0], dato[1], int(dato[2]))
archivo.close()

print(G.DFS('1'))
######################################
