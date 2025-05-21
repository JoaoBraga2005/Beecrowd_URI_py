# -*- coding: utf-8 -*-

A, B, C = input().split()
a = float(A)
b = float(B)
c = float(C)

tri = (a * c)/2
print("TRIANGULO: %.3f"%tri)
pi = 3.14159
cir = pi*(c*c)
print("CIRCULO: %.3f"%cir)
trap = ((a+b)*c)/2
print("TRAPEZIO: %.3f"%trap)
quad = b*b
print("QUADRADO: %.3f"%quad)
ret = a*b
print("RETANGULO: %.3f"%ret)
