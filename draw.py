import xlrd
import define

D=10

fi=xlrd.open_workbook('C:\Users\StMatengss\Desktop\mcm\data.xlsx')
sheet=fi.sheets()[0]
data=sheet.col_values(define.SAT_AVG_ALL)[1:]

res=[]
for i in data:
    if i!='NULL':
        res.append(int(i))

MAX=max(res)
MIN=min(res)
print 'MAX=',MAX
print 'MAX=',MIN

kinds=[0]*D
DIS=(MAX+D-1-MIN)/D
print 'DIS=',DIS

for i in res:
    n=(i-MIN)/DIS
    kinds[n]=kinds[n]+1

SUM=len(res)
means=[0]*D

for i,j in enumerate(kinds):
    print MIN+(i+0.5)*DIS,':',j,',',float(j)/SUM*100,'%'
    means[i]=float(j)/SUM*100

import numpy as np
import matplotlib.pyplot as plt

ind=np.arange(D)
wid=0.5
plt.bar(ind,np.array(means),width=wid,color='red')
plt.show()
