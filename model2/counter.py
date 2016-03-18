import sys,os
import fileinput

count=0
names2=[line[0:len(line)-1] for line in fileinput.input('New Text Document (2).txt')]

for name in names2:
	if name=='NULL':count=count+1

print count

