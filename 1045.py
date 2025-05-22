# -*- coding: utf-8 -*-


a, b ,c = input().split()
A = float(a)
B = float(b)
C = float(c)


if A < B: #se A for menor que B então A vai receber o valor de B
    x  = A
    A = B
    B = x #B agora tem o valor de A

if C > A: #Se C for maior que A então eles trocam de valor
    x = A
    A = C
    C = x

if C < B: #Se apos as trocas entre A, o B for maior que C então eles trocam de valor
    x = B 
    B = C
    C = x


if A >= (B+C):
    print("NAO FORMA TRIANGULO") 
elif A**2 == (B**2) + (C**2):
    print("TRIANGULO RETANGULO")
elif A**2 > (B**2) + (C**2):
    print("TRIANGULO OBTUSANGULO")
elif A**2 < (B**2) + (C**2):
    print("TRIANGULO ACUTANGULO")
if A == B == C:
    print("TRIANGULO EQUILATERO")
elif A == B or B == C or A == C:
    print("TRIANGULO ISOSCELES")
