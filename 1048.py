# -*- coding: utf-8 -*-

s = float(input())

if s <=400:
    novo_s = s + (s*0.15)
    reajuste = s*0.15
    print("Novo salario: %.2f"%novo_s)
    print("Reajuste ganho: %.2f"%reajuste)
    print("Em percentual: 15 %")

elif s <= 800:
    novo_s = s + (s*0.12)
    reajuste = s*0.12
    print("Novo salario: %.2f"%novo_s)
    print("Reajuste ganho: %.2f"%reajuste)
    print("Em percentual: 12 %")

elif s <= 1200:
    novo_s = s + (s*0.1)
    reajuste = s*0.1
    print("Novo salario: %.2f"%novo_s)
    print("Reajuste ganho: %.2f"%reajuste)
    print("Em percentual: 10 %")

elif s <= 2000:
    novo_s = s + (s*0.07)
    reajuste = s*0.07
    print("Novo salario: %.2f"%novo_s)
    print("Reajuste ganho: %.2f"%reajuste)
    print("Em percentual: 7 %")

else:
    novo_s = s + (s*0.04)
    reajuste = s*0.04
    print("Novo salario: %.2f"%novo_s)
    print("Reajuste ganho: %.2f"%reajuste)
    print("Em percentual: 4 %")
