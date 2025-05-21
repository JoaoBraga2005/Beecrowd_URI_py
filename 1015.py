# -*- coding: utf-8 -*-

'''
é necessário a importação da biblioteca math para realizar a raiz
da conta que foi pedida, após isso recebemos os valores em duas linhas
com dois valores cada e as armazenamos em outras variaveis as
tornando float. Após isso é preciso realizar a conta em outra variavel
que guarda o resultado e a raiz desse resultado em outra variavel.
depois é so imprimir usando a função format para aparecer 4 casas
decimais
'''
import math
num1, num2 = input().split()
num3, num4 = input().split()
x1 = float(num1)
y1 = float(num2)
x2 = float(num3)
y2 = float(num4)

dist = ((x2 - x1)**2) + ((y2 - y1)**2)
raiz = math.sqrt(dist)
print("{:.4f}".format(raiz))
