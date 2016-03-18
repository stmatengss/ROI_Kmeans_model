import sys,os
import fileinput

names1=[line[0:len(line)-1] for line in fileinput.input('LOCALE-UGDSUNITID.txt')]
names2=[line[0:len(line)-1] for line in fileinput.input('New Text Document.txt')]

counter=0
mp=dict()

for name in names1:
	mp[name]=1

for name in names1:
	if mp.has_key(name):counter=counter+1

print counter
print len(names1)-counter
print len(names2)-counter
