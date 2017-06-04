import numpy as np
import math
from random import random

numinst=10
repeticiones=10
nevm=1000
densidad=["25", "50", "75", "100"]
salida=open("gaps_difT.txt","w")
def EvaluaBeneficio(x):
    x=np.array(x)
    aux=np.dot(x,q)
    #print(type(aux), type(x))
    sal=np.dot(aux,x.T)
    return sal[0][0]

def EvaluaFactibilidad(x):
    sal=(pm-np.dot(x,w))/pm
    return sal[0]

def generadorSol(mu):
    x=[]
    for s in range(n):
        pot=(1/Temp**2)*(A[s] + np.dot(mu,w)[s])
        if pot > 700:
            pot = 700
        sc=1.0 / (1.0 + math.exp(pot))
        if sc >= 0.5:
            x.append(1)
        else:
            x.append(0)
        sal=[]
        sal.append(x)
    return sal

for ii in densidad:
    for jj in range(numinst):
        instancia="jeu_200/jeu_200_"+str(ii)+"_"+str(jj+1)+".dat"
        nominst="200_"+str(ii)+"_"+str(jj+1)+".dat"
        prom=np.full((1,19),0)
        for kk in range(repeticiones):
            print(nominst)
            re=open(instancia)
            cont=1
            band=0
            q=[]
            error=False
            for linea in re.readlines():
                dato=linea.split("\n")[0]
                dato=dato.split(" ")
                if dato[0] == "0" and cont==1:
                    error=True
                    break
                d=[]
                for i in range(len(dato)):
                    if dato[i] != '':
                        d.append(float(dato[i]))
                if cont == 1:
                    n=int(d[0])
                    pm=int(d[1])
                    op=int(d[2])
                elif cont == 3:
                    w=[]
                    for i in range(n):
                        w.append(d[i])
                elif cont >=  5:
                    q.append(d)
                cont+=1
                re.close()

            if error ==False:
                Temp=1
                solbase=np.full((1,n),1)
                A=np.dot(-(q-np.diag(np.diag(q))), solbase.T)-2*(np.dot(np.diag(np.diag(q)),solbase.T))
                A=A.T[0]
                mui=0.0
                muf=10.0
                mvcm=0
                fmui=EvaluaFactibilidad(generadorSol(mui))
                fmuf=EvaluaFactibilidad(generadorSol(muf))
                while True:
                    if fmui < 0 and fmuf < 0:
                        mui=muf
                        fmui=fmuf
                        muf=3*muf
                        fmuf=EvaluaFactibilidad(generadorSol(muf))
                    else:
                        muc=(mui+muf)/2
                        fmuc=EvaluaFactibilidad(generadorSol(muc))
                        if fmuc < 0:
                            mui=muc
                            fmui=fmuc
                        else:
                            muf=muc
                            fmuf=fmuc
                    difmu=muf-mui
                    if difmu < 0.01:
                        break

                vscmr=EvaluaBeneficio(generadorSol(muf))
                vmm=vscmr
                gap_cm=((op-vscmr)/op)*100
                Temp=5.0
                gaps=[]
                gaps.append(gap_cm)

                while Temp < 15:
                    proboc=[]
                    for s in range(n):
                        pot=(1/Temp**2)*(A[s] + np.dot(muf,w)[s])
                        if pot > 700:
                            pot = 700
                        proboc.append(1.0 / (1.0 + math.exp(pot)))

                    vmm=0
                    for s in range(nevm):
                        a=[random() for i in xrange(n)]
                        c=[i<j for i,j in zip(a,proboc)]
                        solmuestra=[[int(i) for i in c]]
                        factible=EvaluaFactibilidad(solmuestra)
                        if factible >= 0:
                            vm=EvaluaBeneficio(solmuestra)
                            if vm > vmm:
                                vmm=vm
                    gap_mu=((op-vmm)/op)*100
                    gaps.append(gap_mu)
                    Temp+=0.5
                prom=[i+j for (i,j) in zip(prom,gaps)]

        prom=[i/repeticiones for i in prom]
        salida.write(nominst)
        salida.write(" ")
        salida.write(str(list(prom[0]))[1:-2].replace(",",""))##nominst,gaps)
        salida.write("\n")
salida.close()
