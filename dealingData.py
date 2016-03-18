import xlrd
import numpy as np
from numpy import *
import define
import kmeans

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

def noteq(x):
    if x!='PrivacySuppressed' and x!='NULL':return True
    else: return False 

def pending(d):
    res=True
    for i in d:
        res=res and noteq(i)
    return res

fi=xlrd.open_workbook('C:\Users\StMatengss\Desktop\mcm\data.xlsx')
sheet=fi.sheets()[0]
data1=sheet.col_values(define.UNITID)[1:]
data2=sheet.col_values(define.UGDS)[1:]
data3=sheet.col_values(define.SAT_AVG_ALL)[1:]
data4=sheet.col_values(define.md_earn_wne_p10)[1:]
data5=sheet.col_values(define.GRAD_DEBT_MDN_SUPP)[1:]
data6_1=sheet.col_values(define.NPT4_PRIV)[1:]
data6_2=sheet.col_values(define.NPT4_PUB)[1:]
data6=fil(data6_1,data6_2)

xs='LOCALE'
ys='UGDS'
name=[xs,ys]

#tmp=filter(lambda x:(x[0]!='NULL' and x[1]!='NULL'),zip(data1,data2,data3))
tmp=filter(pending,zip(data1,data2,data3,data4,data5,data6))
data=array([x[1:] for x in tmp])
np.savetxt(xs+'-'+ys+'UNITID.txt',array([int(x[0]) for x in tmp]),fmt='%d')

#print data.shape

kmeans.kmeans(data,6,name)


