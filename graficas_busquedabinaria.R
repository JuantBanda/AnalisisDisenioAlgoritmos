datos=read.table("salida.txt", header =TRUE)
print(datos)
pdf(file='grafica_busquedabinaria.pdf', height=5, width=7, onefile=TRUE, family='Helvetica', paper='special', pointsize=12)

par(cex.axis=1.5)
par(cex.lab=1.5)
par(mar = c(5.1,5.1,2,2))
par(oma = c(0,0.7,0,0))
x<- datos$Long

plot(1,1, xlim=c(10,30000), ylim= c(3,31000), xaxt="n", type = "n",
 xlab=expression(Tamaño), ylab=expression(paste(COSTO) ), log="xy")
axis(side= 1, at=x)

colores <- c(colors())
a1 <- datos$prombinT
a2 <- datos$promsimT
a3 <- datos$prombinV
a4 <- datos$promsimV
lines(x, a1, lty=3, lwd=4, col="blue")
lines(x, a2, lty=1, lwd=4, col=colores[84])
lines(x, a3, lty=4, lwd=4, col=colores[283])
lines(x, a4, lty=2, lwd=4, col=colores[384])

legend("topleft", legend=c(expression(binarioT), expression(simpleT),
 expression(binarioV),  expression(simpleV)), lwd=c(4,4,4,4), lty=c(3,1,4,2),
  col=c("blue", colores[84], colores[283], colores[384]) )

dev.off()
