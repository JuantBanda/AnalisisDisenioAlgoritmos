#R CMD BATCH graficas2.R
pdf(file='Output.pdf', height=5, width=7, onefile=TRUE, family='Helvetica', paper='special', pointsize=12)


par(cex.axis=1.5)
par(cex.lab=1.5)
par(mar = c(5.1,5.1,2,2))
par(oma = c(0,0.7,0,0))
x<- c(5,
10,
20,
40,
80,
200,
500,
1000,
5000)

#plot(0,0, xlim=c(25,100), ylim= c(0,0.016), type = "n", xlab=expression( paste( Densidad," ", (italic(d)) )), ylab=expression(GAP) )
plot(0,0, xlim=c(10,5000), ylim= c(0,5000), xaxt="n", type = "n", xlab=expression(Tamaño), ylab=expression(paste(COSTO) ), log="x")
axis(side= 1, at=x)


colores <- c(colors())

a1 <- c(3.4,
4.8,
6.4,
8.15,
10,
12.53,
14.992,
16.974,
21.7288)
a2 <- c(6.4,
10.3,
16.9,
28.65,
50.5,
113.03,
265.492,
517.474,
2522.2288)

a3=c(
  6,
7.8,
9.8,
12,
13.4,
15.7,
18,
20,
25.2
  )
a4=c(
  11,
17.8,
29.8,
52,
93.4,
195.9,
518,
1020,
5025.2
  )
lines(x, a1, lty=3, lwd=4, col=colores[183])
lines(x, a2, lty=1, lwd=4, col=colores[84])
lines(x, a3, lty=4, lwd=4, col=colores[283])
lines(x, a4, lty=2, lwd=4, col=colores[384])

legend("topleft", legend=c(expression(binarioT), expression(simpleT),  expression(binarioV),  expression(simpleV)), lwd=c(4,4,4,4), lty=c(3,1,4,2), col=c(colores[183], colores[84], colores[283], colores[384]) )
#legend(83,8, legend=c(expression(CM), expression(V), expression(a1), expression(a2)), lwd=c(2,2,3,2), lty=c(1,2,3,4), col=c(colores[81],colores[82],colores[183], colores[84]) )

dev.off()
