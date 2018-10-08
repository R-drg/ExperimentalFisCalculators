# coding: utf-8
# calculo desvio padrão
import math
output = open('output.txt', 'w')
input = open('input.txt', 'r')

line = input.readline()
media = float(line)
line = input.readline()
res = 0
cont = 0
while line:
    res=+math.pow((float(line)-media),2)
    line = input.readline()
    cont+=1
res=math.sqrt(res/(cont-1))
output.write(str(res))
