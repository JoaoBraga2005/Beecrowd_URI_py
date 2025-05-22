# -*- coding: utf-8 -*-

a, b, c = input().split()
x = int(a)
y = int(b)
z = int(c)

#x<y<=z
if x > y:
    aux = x
    x = y
    y = aux

if x > z:
    aux = x
    x = z
    z = aux

if z < y:
    aux = y
    y = z
    z = aux

print(x)
print(y)
print(z)
print()
print(a)
print(b)
print(c)
