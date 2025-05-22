# -*- coding: utf-8 -*-

a, b = input().split()
a = int(a)
b = int(b)

if a > b:
    h = (24 - a) + b
    print("O JOGO DUROU %d HORA(S)"%h)

elif a == b:
    h = 24
    print("O JOGO DUROU %d HORA(S)"%h)

elif a < b:
    h = b -a
    print("O JOGO DUROU %d HORA(S)"%h)
