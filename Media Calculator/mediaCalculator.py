# coding: utf-8
# calculo da média
output = open('output.txt', 'w')
input = open('input.txt', 'r')

line = input.readline()
res= 0
cont=0
while line:
    res += float(line)
    line = input.readline()
    cont+=1
output.write(str(res/cont))
