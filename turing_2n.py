reglas=dict()

reglas['s0']=['s',0,1]
reglas['s1']=['s',1,1]
reglas['se']=['alto',0,0]
reglas['sp']=['s','p',1]

numero=2000
bin0=(bin(numero)[2:])
numbin0=[]
for i in bin0:
    numbin0.append(int(i))
cinta=['p']+numbin0+['e']
edo='sp'
puntero=0
while True:
    cinta[puntero]=reglas[edo][1]
    puntero+=reglas[edo][2]
    edo=reglas[edo][0]+str(cinta[puntero])
    if(reglas[edo][0]=='alto'):
        cinta[puntero]=reglas[edo][1]
        break
numbin1=cinta[1:len(cinta)]

aux=''
for i in numbin1:
    aux+=str(i)
num1=int(str(aux), 2)

print("Num:",numero,"Num+1:", num1)
