# -*- coding: utf-8 -*-

strg1 = input()
strg2 = input()
strg3 = input()

if strg1 == "vertebrado":
    if strg2 == "ave":
        if strg3 == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if strg3 == "onivoro":
            print("homem")
        else:
            print("vaca")

if strg1 == "invertebrado":
    if strg2 == "inseto":
        if strg3 == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if strg3 == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")
