x=read.csv("datos-transfase.csv", head=FALSE)
print(x)
temp=c()
print(temp)
for(i in 10:29){
  temp=c(temp,rep(i/2,10))
}

####################################
gaps=c()
for(i in 3:22){
  aux=paste("V",i, sep="")
  y=x[aux]
  gaps=c(gaps,y[1:10,] )
}
pdf(file='diagcajas25.pdf', height=5, width=7, onefile=TRUE, family='Helvetica', paper='special', pointsize=12)
boxplot(gaps ~ temp, data = x , at=1:20, col = "lightgray",xlab="Temperatura", ylab="GAP %", main="Densidad del 25%")#, names=c("a","b", "c","d","e","f","g","h","i"))
dev.off()
####################################
gaps=c()
for(i in 3:22){
  aux=paste("V",i, sep="")
  y=x[aux]
  gaps=c(gaps,y[11:20,] )
}
pdf(file='diagcajas50.pdf', height=5, width=7, onefile=TRUE, family='Helvetica', paper='special', pointsize=12)
boxplot(gaps ~ temp, data = x , at=1:20, col = "lightgray",xlab="Temperatura", ylab="GAP %", main="Densidad del 50%")#, names=c("a","b", "c","d","e","f","g","h","i"))
dev.off()
####################################
gaps=c()
for(i in 3:22){
  aux=paste("V",i, sep="")
  y=x[aux]
  gaps=c(gaps,y[21:30,] )
}
pdf(file='diagcajas75.pdf', height=5, width=7, onefile=TRUE, family='Helvetica', paper='special', pointsize=12)
boxplot(gaps ~ temp, data = x , at=1:20, col = "lightgray",xlab="Temperatura", ylab="GAP %", main="Densidad del 75%")#, names=c("a","b", "c","d","e","f","g","h","i"))
dev.off()
####################################
gaps=c()
for(i in 3:22){
  aux=paste("V",i, sep="")
  y=x[aux]
  gaps=c(gaps,y[31:40,] )
}
pdf(file='diagcajas100.pdf', height=5, width=7, onefile=TRUE, family='Helvetica', paper='special', pointsize=12)
boxplot(gaps ~ temp, data = x , at=1:20, col = "lightgray",xlab="Temperatura", ylab="GAP %", main="Densidad del 100%")#, names=c("a","b", "c","d","e","f","g","h","i"))
dev.off()
