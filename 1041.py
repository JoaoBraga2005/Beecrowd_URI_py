# -*- coding: utf-8 -*-

x, y = input().split()
x = float(x)
y = float(y)
if (x==y==0):
    print("Origem")
elif(x==0):
    print("Eixo Y")
elif(y==0):
    print("Eixo X")
elif(x>0)and(y>0):
    print("Q1")
elif(x<0)and(y>0):
    print("Q2")
elif(x<0) and (y<0):
    print("Q3")
elif(x>0)and(y<0):
    print("Q4")
