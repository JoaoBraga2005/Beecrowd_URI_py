# -*- coding: utf-8 -*-

'''
Para este exercicio devemos utilizar uma conta básica que nos dará
a quantidade total de quilometros da viagem e então dividir por 12,
que é a quantidade de KM/L do exemplo. Recebemos os valores da hora
e quilometros e os armazenamos. apos isso em uma variavel x realizamos
o total de kms e em outra variável dividimos x por 12 e temos o 
total de litros de gasolina.
'''
h = int(input())
km = int(input())

x = h * km
total_gasolina = x/12
print("{:.3f}".format(total_gasolina))
