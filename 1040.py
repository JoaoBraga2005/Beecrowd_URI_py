# -*- coding: utf-8 -*-

n, n2, n3, n4 = input().split()
N1 = float(n)
N2 = float(n2)
N3 = float(n3)
N4 = float(n4)

media = ((N1 * 2) + (N2*3) + (N3*4) + (N4*1))/10
if media >= 7:
    print("Media: %.1f" % media)
    print("Aluno aprovado.")
elif media < 5:
    print("Media: %.1f" % media)
    print("Aluno reprovado.")
else:
    print("Media: %.1f" % media)
    print("Aluno em exame.")
    ex = float(input())
    mediafinal = (media + ex)/2
    if media >= 5:
        print("Nota do exame: %.1f" % ex)
        print("Aluno aprovado.")

    else:
        print("Nota do exame: %.1f" % ex)
        print("Aluno reprovado.")
    print("Media final: %.1f" % mediafinal)
        


        
