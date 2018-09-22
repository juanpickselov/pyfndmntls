from math import factorial as fac

n = 5
k = 3
fac_5 = fac(5)
fac_6 = fac(6)

print(fac(n) // (fac(k) * fac(n - k)))
print(fac_5)
print(fac_6)
print(fac(100))
print(len(str(fac(100))))
print(fac(13))
