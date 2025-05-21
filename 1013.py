# -*- coding: utf-8 -*- 

num1, num2, num3 = input().split()
a = int(num1)
b = int(num2)
c = int(num3)

mAB = (a + b + abs(a - b))/2
mTodos = (mAB + c + abs(mAB - c))/2
print(f"{mTodos:.0f} eh o maior")
