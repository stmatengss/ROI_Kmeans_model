import sys,os

names2=[line[0:len(line)-1] for line in fileinput.input('New Text Document(2).txt')

counter=0

for name in names:
	if name=='NULL':counter=counter+1

print counter

