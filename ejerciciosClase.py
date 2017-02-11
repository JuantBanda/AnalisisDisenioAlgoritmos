from math import log, exp
def binom_exacto(n,k):
    mayor=max(n-k,k)
    menor=min(n-k,k)
    prod=1
    for x in range(mayor+1, n+1):
        prod*=x
    otro_prod=1
    for x in range(2, menor+1):
        otro_prod*=x
    return prod/otro_prod

def binom_aprox(n,k):
    mayor=max(n-k,k)
    menor=min(n-k,k)
    slogarriba=0
    for x in range(mayor+1, n+1):
        slogarriba+=log(x)
    slogabajo=0
    for x in range(2, menor+1):
        slogabajo+=log(x)
    return exp(slogarriba-slogabajo)

n=200
k=100
ce=binom_exacto(n,k)
ca=binom_aprox(n,k)

print(ce)
print(ca)


r=1
num=1111643
v = num
pot = 2567140
mod = 123
potencia = pot
while potencia > 0:
    if potencia % 2 == 1:
        r *= v
        r = r % mod
    potencia = potencia >> 1
    v *= v
    v = v % mod
print(r)
print(num**pot % mod)
