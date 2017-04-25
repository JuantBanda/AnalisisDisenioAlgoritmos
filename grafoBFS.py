
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

G = grafo()
archivo=open("instancia_grafo.txt", "r")
for linea in archivo.readlines():
    dato=linea.split("\n")[0]
    dato=dato.split(" ")
    G.conecta(dato[0], dato[1], int(dato[2]))
archivo.close()

print(G.vecinos)

capa=0
semilla="3"
nivel = {semilla: capa}
agregados = {semilla}
while len(agregados) > 0:
    capa += 1
    siguientes = set()
    for wey in agregados:
        for w in G.vecinos[wey]:
            if w not in nivel:
                nivel[w] = capa
                siguientes.add(w)
    agregados = siguientes
print(nivel)

