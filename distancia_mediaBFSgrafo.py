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

    def BFS(self,semilla):
        capa=0
        #semilla="1"
        nivel = {semilla: capa}
        agregados = {semilla}
        while len(agregados) > 0:
            capa += 1
            siguientes = set()
            for wey in agregados:
                for w in self.vecinos[wey]:
                    if w not in nivel:
                        nivel[w] = capa
                        siguientes.add(w)
            agregados = siguientes
        return nivel

##########################################
G = grafo()
archivo=open("instancia_grafo.txt", "r")
for linea in archivo.readlines():
    dato=linea.split("\n")[0]
    dato=dato.split(" ")
    G.conecta(dato[0], dato[1], int(dato[2]))
archivo.close()
#########distancia media de un grafo########################################
sm_dmv=0
for x in G.nodos:
    d=G.BFS(x)
    sm=0
    for y in G.nodos:
        sm+=d[y]
    dmv=(1/(len(G.nodos)-1))*sm#distancia promedio del nodo v con elresto
    print("Distancia media del nodo", x, "con el resto",dmv)
    sm_dmv+=dmv

dmG=(1/(2*len(G.nodos)))*sm_dmv#distancia media del grafo
print(">Distancia media del grafo>>>", dmG)

