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

fi=xlrd.open_workbook('2911 - New - ToDo.xlsx')
sheet=fi.sheets()[0]
data1=sheet.col_values(0)[1:]
data2=sheet.col_values(1)[1:]
data3=sheet.col_values(2)[1:]
data4=sheet.col_values(3)[1:]
data5=sheet.col_values(6)[1:]


xs='UNITID'
ys=''
name=[xs,ys]

#tmp=filter(lambda x:(x[0]!='NULL' and x[1]!='NULL'),zip(data1,data2,data3))
tmp=filter(pending,zip(data1,data2,data3,data4,data5))
data=array(map(lambda x:(x[1],x[2],x[3],100.0/x[4]),tmp))
np.savetxt(xs+'-'+ys+'-UNITID.txt',array([int(x[0]) for x in tmp]),fmt='%d')

kmeans.kmeans(data,4,name)



