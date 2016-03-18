#factors

import sys,os
import numpy as np
import xlrd
import define
from numpy import *
import matplotlib.pyplot as plt

AVE=0

def fil(d1,d2):
    res=[]
    for x,y in zip(d1,d2):
        if x!='NULL':
            res.append(x)
        elif y!='NULL':
            res.append(y)
        else:
            res.append('NULL')
    return res

def pending(x):
    if x[10]==1:return True
    else: return False

def pending2(x):
    res=[]
    for i in x:
        if i=='NULL':res.append(0)
        else :res.append(1)
    return res

def cal(x):
    global AVE
    if x=='NULL' or x=='PrivacySuppressed':return AVE
    else: return float(x)

D1=0.2
D2=0.4
D3=0.4
STD=np.array([7,3,3,2,2,2,4,4,1,1,0])


fi=xlrd.open_workbook('C:\Users\StMatengss\Desktop\mcm\data.xlsx')
sheet=fi.sheets()[0]

data1=sheet.col_values(define.HCM2)[1:]
data2=sheet.col_values(define.UGDS)[1:]
data3=sheet.col_values(define.SAT_AVG_ALL)[1:]
data4=sheet.col_values(define.md_earn_wne_p10)[1:]
data5=sheet.col_values(define.GRAD_DEBT_MDN_SUPP)[1:]
data6_1=sheet.col_values(define.NPT4_PRIV)[1:]
data6_2=sheet.col_values(define.NPT4_PUB)[1:]
data6=fil(data6_1,data6_2)
data7=sheet.col_values(define.RPY_3YR_RT_SUPP)[1:]
data8_1=sheet.col_values(define.C150_4_POOLED_SUPP)[1:]
data8_2=sheet.col_values(define.C200_L4_POOLED_SUPP)[1:]
data8=fil(data8_1,data8_2)
data9_1=sheet.col_values(define.PCTFLOAN)[1:]
data9_2=sheet.col_values(define.PCTPELL)[1:]
data9=fil(data9_1,data9_2)
data10=sheet.col_values(define.UG25abv)[1:]
data11=sheet.col_values(define.CURROPER)[1:]

tmp=filter(pending,zip(data1,data2,data3,data4,\
                       data5,data6,data7,data8,\
                       data9,data10,data11))
part1=np.sum(np.array(map(pending2,tmp),dtype=float)*STD,axis=1)/29
print part1

#data7 & data8
data7=[x[6] for x in tmp]
data8=[x[7] for x in tmp]

#print data7
#print data8

tmp=np.array(map(cal,filter(lambda x:x!='NULL' and x!='PrivacySuppressed',data7)))
AVE=np.mean(tmp)
part2=np.array(map(cal,data7))

tmp=np.array(map(cal,filter(lambda x:x!='NULL' and x!='PrivacySuppressed',data8)))
AVE=np.mean(tmp)
part3=np.array(map(cal,data8))

print part2

print part3

res=part1*D1+part2*D2+part3*D3

x=np.arange(0,1.01,0.01)
y=np.zeros(101)
print res
for i in res:
    n=int(i*100)
    y[n]=y[n]+1

tmp=0.0

for i,j in enumerate(y):
    tmp=tmp+j
    y[i]=tmp

plt.plot(x,y)
plt.xlabel('risk-factor')
plt.ylabel('sum of schools')
#plt.hist(res,100)
plt.show()











