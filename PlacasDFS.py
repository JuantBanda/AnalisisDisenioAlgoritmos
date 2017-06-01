from PIL import Image
from sys import argv
from math import ceil


blanco = (255,255,255)
negro = (0,0,0)

input1=argv[1]
im = Image.open(input1)
width, height = im.size
pixelMap = im.load()


print "ancho", width, "alto", height
img = Image.new(im.mode, im.size)
pixelsNew = img.load()


visitados=set()
negros=set()
for i in range(width):
    for j in range(height):
            red, green, blue = pixelMap[i,j]
            #print red, green, blue
            g = 1.0 * (red + green + blue) / 3
            if g < 60:
                pixelsNew[i,j] = negro
                negros.add((i,j))
            else:
                pixelsNew[i,j] = blanco
                #visitados.add((i,j))

            #elif g > 250
            #    pixelsNew[i,j] = blanco
            #else:
            #    pixelsNew[i,j] = int(ceil(255 * ((1.0)*(g - 10) / 240)))

#print(negros)
inicio=(0,0)
visitados.add(inicio)
pila=[inicio]
print(pila)
base=inicio
nx=0
ny=0
while len(pila)!=0:
    cont=0
    for ix in xrange(-1,1):
        for iy in xrange(-1,1):
            if base[0]>0 and base[0]<width:
                nx=base[0]+ix
            if base[1]>0 and base[1]<height:
                ny=base[1]+iy
                visitados.add((nx,ny))
            #print nx, ny
            #print(visitados)

#pixelsNew[1,1]= (255,0,0)
#pixelsNew[1,2]= (255,0,0)
#def DFS(x,y):
#    pila=[(x,y)]

    #visitados.add((1,1))
    #print(visitados)
#    return pila

#print(DFS(0,0))
#print(visitados)
#print(inicio in  visitados)
img.save(input1.replace(".jpg","")+"_BN.png")
