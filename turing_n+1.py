reglas=dict()
reglas['s0']=['s',0,1]
reglas['s1']=['s',1,1]
reglas['se']=['q','e',-1]
reglas['sp']=['s','p',1]
reglas['q0']=['alto',1,0]
reglas['q1']=['q',0,-1]
reglas['qp']=['alto','p',1] 

numero=2016
bin0=(bin(numero)[2:])
numbin0=[]
for i in bin0:
    numbin0.append(int(i))
cinta=['p']+numbin0+['e']
edo='sp'
puntero=0
while True:
    #print(edo)
    #print(cinta)
    cinta[puntero]=reglas[edo][1]
    puntero+=reglas[edo][2]
    edo=reglas[edo][0]+str(cinta[puntero])
    if(reglas[edo][0]=='alto'):
        cinta[puntero]=reglas[edo][1]
        break
numbin1=cinta[1:len(cinta)-1]

aux=''
for i in numbin1:
    aux+=str(i)
num1=int(str(aux), 2)

print("Num:",numero,"Num+1:", num1)
