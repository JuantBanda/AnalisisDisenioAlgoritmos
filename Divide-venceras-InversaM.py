from numpy import matrix,zeros, array
M= matrix([[1,3,-5, 4],[0,-5,17,-11],[0,0,164.0/5,-77.0/5],[0,0,0,117.0/82]])
n=len(M)
L11=zeros((n/2,n/2))
L12=zeros((n/2,n/2))
L22=zeros((n/2,n/2))
L21=zeros((n/2,n/2))
inversaM=zeros((n,n))

for i in range(n):
    for j in range(n):
        if i < n/2 and j < n/2:
            L11[i,j] = M[i,j]
        if i < n/2 and j >= n/2:
            L12[i-n/2,j-n/2] = M[i,j]
        if i >=n/2 and j >= n/2:
            L22[i-n/2,j-n/2]=M[i,j]
L11=matrix(L11)
L12=matrix(L12)
L22=matrix(L22)
L21=matrix(L21)
IL11=L11.I
IL22=L22.I
PI=-IL11*L12*IL22
for i in range(n):
    for j in range(n):
        if i < n/2 and j < n/2:
            inversaM[i,j] = IL11[i,j]
        if i < n/2 and j >= n/2:
            inversaM[i,j] = PI[i, j-n/2]
        if i >=n/2 and j >= n/2:
            inversaM[i,j] = IL22[i-n/2, j-n/2]


print(inversaM)

#M= matrix([[1,3,-5, 4],[3, 4, 2, 1],[-5, 2, 0, 2 ],[1, 5,7, 1]])

#print(triu_indices(M))
#con=1
#for i in range(n-1):
#    for j in range(n-1):
        #elim=-M[j+1,i]
        #print(i,j)
        #for k in range(n):


        #M[i,j+1]+=piv
#        if j+con < n:
#            print(j+con,i)
#            elim=-float(M[j+con,i])
#            print(elim)
#            if elim != 0:
#                cte=elim/M[j+con-1,i]
            #    print(cte)
            #    for k in range(n-1):
            #        M[j+con,k]+=cte*M[j+con-1,i]
#    con += 1
