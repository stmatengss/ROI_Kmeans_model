import xlrd
import numpy as np
from numpy import *
import define
import kmeans
import math
import matplotlib.pyplot as plt


fi=xlrd.open_workbook('C:\Users\StMatengss\Desktop\mcm\data.xlsx')
sheet=fi.sheets()[0]
data1=sheet.col_values(define.SAT_AVG_ALL)[1:]
data2_1=sheet.col_values(define.ACTCMMID)[1:]
data2_2=sheet.col_values(define.ACTENMID)[1:]
data2_3=sheet.col_values(define.ACTMTMID)[1:]

data=[]

for x in zip(data1,data2_1,data2_2,data2_3):
    res=True
    for y in x:
        res=res and (y!='NULL' and y!='PrivacySuppressed' and y!='')
    if res==True:
        try:
            data.append((int(x[0]),(int(x[1])+int(x[2])+int(x[3]))))
        except:
            print x
data=np.array(data)

for i in range(data.shape[0]):
    plt.plot(data[i,0],data[i,1],'og')
plt.xlabel('SAT_AVG')
plt.ylabel('ACT_TOTAL')
plt.show()
