# -*- coding: utf-8 -*-

nome = input()
sal = float(input())
vendas = float(input())

bonus = (vendas * (15/100)) + sal
print("TOTAL = R$ %.2f"%bonus)
