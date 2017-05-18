#Algoritmo Prim con conectividad media y distribución uniforme.
from time import sleep
from random import choice, randint
from math import ceil
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
        candidatos=set()
        checados=set()
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

    def conexo(self):
        for com in self.nodos:
            ini=com
            break
        for fin in self.nodos:
            if fin != ini:
                #print(ini, fin)
                if self.camino(ini,fin)==False:
                    return False
        return True

    def prim(self):
        if self.conexo() == True:
            print('Se puede usar el método')
            for i in self.nodos:
                ni=i
                break
        #    print('nodo inicial',ni)
        #    print("vecinos",self.vecinos[ni])

            vt=self.nodos
            aa=set() #aristas agregadas
            va=set() #vértices agregados
            va.add(ni)
            while va != vt:
                minw=1e10
                for u in va:
                    for v in self.vecinos[u]:
                        if self.aristas[(u,v)] < minw and v not in va:
                            uv=(u,v)
                            minw=self.aristas[(u,v)]
                            vv=v
                aa.add(uv)
                va.add(vv)
                #input()
                #sleep(1)
            suma=0
            for i in aa:
                suma+=self.aristas[i]
            salida=list()
            salida.append(suma)
            salida.append(aa)
            #print(salida)
            return salida
        else:
            print('no se puede usar el método ya que el grafo no es conexo')

def generainst_conmed_unif(nodos):
    aristas=ceil(nodos*(nodos-1)/4)
    ci=1
    cs=1000
    archivo="inst_conmed_unif.txt"
    salida=open(archivo,"w")
    print('a','b','peso',file=salida)
    arcos=[]
    auxarc=[]
    for m in range(nodos):
        for n in range(nodos):
            if (m,n) not in arcos and m != n:
                arcos.append((m,n))
                arcos.append((n,m))
                auxarc.append((m,n))
    cont=0
    while cont<aristas:
        ab=choice(auxarc)
        auxarc.remove(ab)
        peso=randint(ci,cs)
        print(ab[0]+1,ab[1]+1,peso,file=salida)
        print(ab[1]+1,ab[0]+1,peso,file=salida)
        cont+=1

    salida.close()


G = grafo()


archivo=open("inst_conmed_unif.txt", "r")
band=0
for linea in archivo.readlines():
    if band !=0:
        dato=linea.split("\n")[0]
        dato=dato.split(" ")
        G.conecta(dato[0], dato[1], int(dato[2]))
    band=1

archivo.close()

generainst_conmed_unif(5)
print('suma de pesos y aristas del árbol de expansión:', G.prim())
