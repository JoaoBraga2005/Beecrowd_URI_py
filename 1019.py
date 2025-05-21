# -*- coding: utf-8 -*-

N = int(input())
X = N // 3600
Y = (N % 3600) // 60
Z = (((N % 3600) % 3600) % 60)
print("%d:%d:%d" % (X, Y, Z))
