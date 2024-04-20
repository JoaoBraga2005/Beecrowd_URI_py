# -*- coding: utf-8 -*-
"""
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.
"""
a, b = input().split()
x = int(a)
y = float(b)

if x == 1:
    y = y*4
    print("Total: R$ {:.2f}".format(y))
elif x == 2:
    y = y*4.50
    print("Total: R$ {:.2f}".format(y))
elif x == 3:
    y = y*5.00
    print("Total: R$ {:.2f}".format(y))
elif x == 4:
    y = y*2.00
    print("Total: R$ {:.2f}".format(y))
else:
    y = y*1.50
    print("Total: R$ {:.2f}".format(y))
