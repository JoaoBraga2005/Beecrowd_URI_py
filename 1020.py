# -*- coding: utf-8 -*-

'''
Recebemos o total de dias e atribuimos a variavel ano e dividimos
de forma inteira para descobrir a quantidade de anos. para 
descobrir os meses e os dias temos que saber o resto da divisão
dos anos e então dividr de forma inteira por 30 para descobrir o mes
e o resto desta divisão será a quantidade de dias.
'''
total_dias = int(input())
ano = total_dias // 365
ano_restante = total_dias % 365
mes = ano_restante // 30
dia = ano_restante % 30
print(ano, "ano(s)")
print(mes, "mes(es)")
print(dia, "dia(s)")
