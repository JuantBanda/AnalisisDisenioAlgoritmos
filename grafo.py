
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
        print(checados)
        print(candidatos)
        #band=True
        while(True):
            if len(candidatos)==0:
                return False
                break
            base=candidatos.pop()
            print(base)
            for j in range(len(self.salidas[base])):
                punt=self.salidas[base][j]
                if punt==final:
                    return True
                    #band=False
                    #break

                if punt not in checados:
                    candidatos.add(punt)






G = grafo()
G.conecta('a', 'b', 1)
G.conecta('b', 'c', 2)
G.conecta('c', 'd', 3)
#G.conecta('a', 'd', 4)
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
print("salidas totales:", G.salidas)

#del G.salidas['a'][0]
#print(G.salidas)
print("--------------------------------------------")

print("Hay un camino de 'a' a 'd'?")
print(G.camino("a", "d"))
inicio="a"
final="c"
base=inicio
checados=set()
candidatos=set()
checados.add(base)
candidatos.add(base)
print(checados)
print(candidatos)

#print("d" in G.salidas[base])
x=True
while(x==True):
    if len(candidatos)==0:
        print("no hay camino")
        break
    base=candidatos.pop()
    print(base)
    for j in range(len(G.salidas[base])):
        punt=G.salidas[base][j]
        if punt==final:
            print("si hay camino")
            x=False
            break

        if punt not in checados:
            candidatos.add(punt)
    #candidatos.remove(base)

print('********')
print(checados)
print(candidatos)
