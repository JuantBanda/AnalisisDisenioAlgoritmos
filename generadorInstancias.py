from random import choice, randint
def genera_instancias():
    num_inst=input("Introduce número pruebas a generar: ")
    try:
        num_inst=int(num_inst)
    except:
        print("Error, valor no numérico.")
        return

    print("Introduce el rango de valores de los pesos")
    ci=input("*valor menor: ")
    cs=input("*valor mayor: ")
    try:
        ci=int(ci)
        cs=int(cs)
    except:
        print("Error de captura, valor no numérico.")
        return
    if cs<=ci:
        print("Error lógico")
        return

    print("Teclea la letra correspondiente según el tipo de grafo preferente")
    tipo=input("*Grafo no dirigido >> nd, Grafo dirigido >> d: ")
    if not(tipo=="d" or tipo=="nd"):
        print("Error de captura, argumento inválido.")
        return

    nodos=input("Introduce el número de nodos: ")
    try:
        nodos=int(nodos)
    except:
        print("Error de captura, valor no numérico.")
        return

    aristas=input("Introduce el número de aristas: ")
    try:
        aristas=int(aristas)
    except:
        print("Error de captura, valor no numérico")
        return

    if tipo=="nd" and aristas > (1/2)*nodos*(nodos-1):
        print("Error, el número de aristas no debe ser mayor a: ", (1/2)*nodos*(nodos-1))
        return

    if tipo=="d" and aristas > nodos*(nodos-1):
        print("Error, el número de aristas no debe ser mayor a: ", nodos*(nodos-1))
        return

    for i in range(num_inst):
        if tipo=="d":
            archivo="instancia%i%s"%((i+1),tipo)+".txt"
            salida=open(archivo,"w")
            print('a','b','peso',file=salida)
            arcos=[]
            auxarc=[]
            for m in range(nodos):
                for n in range(nodos):
                    if (m,n) not in arcos and m != n:
                        arcos.append((m,n))
                        arcos.append((n,m))
            cont=0
            while cont < aristas:
                ab=choice(arcos)
                arcos.remove(ab)
                peso=randint(ci,cs)
                print(ab[0]+1,ab[1]+1,peso,file=salida)
                cont+=1
        else:
            archivo="instancia%i%s"%((i+1),tipo)+".txt"
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

genera_instancias()
