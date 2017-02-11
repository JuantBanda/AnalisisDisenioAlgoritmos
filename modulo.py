r=1
num=11116
v = num
pot = 256710
mod = 123
potencia = pot
while potencia > 0:
    if potencia % 2 == 1:
        r *= v
        r = r % mod
    potencia = potencia >> 1
    v *= v
    v = v % mod
print("Valor con truco: ",r, "Valor librería:", num**pot % mod)
