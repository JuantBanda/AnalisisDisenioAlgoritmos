import numpy as np
import math
datos=open("uf50-01.cnf", "r")
satw=[]
for linea in datos:
    linea.strip()
    p=linea.split()
    satw+=p
datos.close()
nvar=int(satw[26])
nres=int(satw[27])
satw=satw[28:(nres*4+27)]
satw=[int(i) for i in satw]
print "num restricciones",nres
print "num de variables", nvar

w=np.zeros((nres,nvar))
r=0
for s in range(len(satw)):
    if satw[s]==0:
        r+=1
    else:
        n=abs(satw[s])
        if satw[s]<0:
            w[r][n-1]=-1
        elif satw[s]>0:
            w[r][n-1]=1
        else:
            w[r][n-1]=0

mu=np.full((1,nres),1)
mnviol=10000000000
nomejora=0
while True:
    ve=np.dot(-mu, w)
    m=np.full((1,nvar),0)
    x=np.full((1,nvar),0)
    falsos=[] 
    for s in range(nvar):
        m[0][s]=1/(1+math.exp(ve[0][s]))
        if m[0][s]>=.5:
            x[0][s]=1
        else:
            falsos.append(s)
    for i in range(len(falsos)):
        x[0][falsos[i]]=-1
    rclau=np.dot(w,x.T)
    nviol=0
    for i in range(nres):
        if rclau[i][0]==-3:
            nviol+=1
            mu[0][i]=mu[0][i]+.01
    if nviol<mnviol:
        mnviol=nviol
        print "Clausulas violadas:", mnviol
        nomejora=0
    nomejora+=1
    if nomejora==10000:
        break
