# -*- coding: utf-8 -*-

ced = float(input())

not100 = ced // 100
ced = ced - not100*100

not50 = ced // 50
ced = ced - not50*50

not20 = ced // 20
ced = ced - not20*20

not10 = ced // 10
ced = ced - not10*10

not5 = ced // 5
ced = ced - not5*5

not2 = ced // 2
ced = ced - not2*2

moed1 = ced // 1
ced = ced - moed1*1

moed50 = ced // 0.5
ced = ced - moed50*0.5

moed25 = ced // 0.25
ced = ced - moed25*0.25

moed10 = ced // 0.10
ced = ced - moed10*0.10

moed05 = ced // 0.05
ced = ced - moed05*0.05

moed01 = ced * 100

print("NOTAS:")
print("%.0f"%not100, "nota(s) de R$ 100.00")
print("%.0f"%not50, "nota(s) de R$ 50.00")
print("%.0f"%not20, "nota(s) de R$ 20.00")
print("%.0f"%not10, "nota(s) de R$ 10.00")
print("%.0f"%not5, "nota(s) de R$ 5.00")
print("%.0f"%not2, "nota(s) de R$ 2.00")
print("MOEDAS:")
print("%.0f"%moed1, "moeda(s) de R$ 1.00")
print("%.0f"%moed50, "moeda(s) de R$ 0.50")
print("%.0f"%moed25, "moeda(s) de R$ 0.25")
print("%.0f"%moed10, "moeda(s) de R$ 0.10")
print("%.0f"%moed05, "moeda(s) de R$ 0.05")
print("%.0f"%moed01, "moeda(s) de R$ 0.01")
