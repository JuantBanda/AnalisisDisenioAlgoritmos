import string
from random import randint

def triplesat(A, linea, tipo, Nclau):
    if tipo=="cnf":
        for j in range(Nclau):#clausulas
            k=0
            for i in range(3):
                var=linea.split()[3*j+k]
                neg = False
                checa = var
                if '!' in var:
                    neg = True
                    checa = var[1:]
                cierto = (checa in A)
                if neg:
                    cierto = not cierto
                if i==2 and cierto==False:
                    return False
                if cierto==True:
                    break
                k+=1
        return True
    else:
        #DNF
        cuentaTrue=0
        for j in range(Nclau):#clausulas
            k=0
            for i in range(3):
                var=linea.split()[3*j+k]
                neg=False
                checa=var
                if '!' in var:
                    neg = True
                    checa = var[1:]
                cierto = (checa in A)
                if neg:
                    cierto = not cierto 
                if(cierto==False):
                    break
                k+=1
            if k==3:
                return True
        return False


A = set("x y r".split())
linea = "!x !y z z y !q !p x r"
print(triplesat(A, linea, "dnf", 3))

letras=string.ascii_lowercase
B=set()
linea=''
nclau=5
for k in range(3*nclau):
    if randint(0,1)==1:
        B.add(letras[randint(0,len(letras)-1)])
    if randint(0,1):
        linea+='!'
        linea+=letras[randint(0,len(letras)-1)]
        linea+=' '
    else:
        linea+=letras[randint(0,len(letras)-1)]
        linea+=' '

print(B)
print(linea)
print(triplesat(B, linea, "dnf", nclau))
