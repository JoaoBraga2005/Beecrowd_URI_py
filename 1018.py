# -*- coding: utf-8 -*-

'''
Primeiro recebemos o valor inteiro e na primeira variavel para
contar as cédulas de 100 dividimos de forma inteira por 100, para
as outras cédulas iremos sempre fazer o resto dos valores 
anteriores divido de forma inteira pelo valor da cédula que 
queremos.
 '''
ced = int(input())
not100 = ced // 100
not50 = (ced % 100) // 50
not20 = ((ced % 100) % 50) // 20
not10 = (((ced % 100) % 50) % 20) // 10
not5 = ((((ced % 100) % 50) % 20) % 10) // 5
not2 = (((((ced % 100) % 50) % 20) % 10) % 5) // 2
not1 = ((((((ced % 100) % 50) % 20) % 10) % 5) % 2) // 1
print(ced)
print(not100, "nota(s) de R$ 100,00")
print(not50, "nota(s) de R$ 50,00")
print(not20, "nota(s) de R$ 20,00")
print(not10, "nota(s) de R$ 10,00")
print(not5, "nota(s) de R$ 5,00")
print(not2, "nota(s) de R$ 2,00")
print(not1, "nota(s) de R$ 1,00")
