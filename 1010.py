# -*- coding: utf-8 -*-

a, b, c = input().split()
d, e, f = input().split()
a = int(a)
b = int(b)
c = float(c)

d = int(d)
e = int(e)
f = float(f)

total = (b*c) + (e*f)
print("VALOR A PAGAR: R$ %.2f"%total)
