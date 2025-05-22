# -*- coding: utf-8 -*-

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
if a < b + c and b < c+  a and c < a + b:
    perimetro = a+c+b
    print("Perimetro = %.1f"%perimetro)
else:
    area = ((a+b)*c)/2
    print("Area = %.1f"%area)
