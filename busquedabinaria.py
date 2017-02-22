from random import randint

COSTO = 0

def binaria(x, c):
    global COSTO
    largo = len(x)
    if largo == 0:
        return False
    mitad = largo // 2
    COSTO += 1
    if c == x[mitad]:
        return True
    COSTO += 1
    if c > x[mitad]:
        return binaria(x[mitad+1:], c)
    return binaria(x[:mitad], c)

def gen(cuantos):
    x = [randint(0,100)]
    for i in range(cuantos-1):
        x.append(x[-1] + randint(1, 100))
    return x

def simple(x,c):
    global COSTO
    for i in range(len(x)):
        COSTO += 1
        if x[i] == c:
            return True
    return False
print("Long","prombinT", "prombinV",  "promsimT", "promsimV")
for L in [5,10, 20, 40, 80, 200, 500,1000, 5000]:
    arreglo = gen(L)
    sumabin=0
    sumasim=0
    for a in arreglo:
        #ciclo que regresa el costo de de buscar en la lista un elemento de la lista
        COSTO = 0
        assert binaria(arreglo, a) == True
        #print('bin', True, L, COSTO)
        sumabin+=COSTO
    #print('binT', L, prombinT)

        assert simple(arreglo, a) == True
        sumasim+=COSTO
    prombinT=sumabin/L
    promsimT=sumasim/L
        #print('sim', True, L, COSTO)
    sumabin=0
    sumasim=0
    N=10
    for i in range(N):
        #ciclo que regresa el costo de de buscar en la lista un elemento aleatorio
        a = randint(10, 200)
        COSTO = 0
        incl = (a in arreglo)
        assert binaria(arreglo, a) == incl
        #print('bin', incl, L, COSTO)
        sumabin+=COSTO
        assert simple(arreglo, a) == incl
        sumasim+=COSTO
        #print('sim', incl, L, COSTO)
    prombinV=sumabin/N
    promsimV=sumasim/N
    #print('binV', L, sumabin/N)
    print(L,prombinT, prombinV, promsimT, promsimV)
