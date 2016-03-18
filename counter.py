import xlrd
import numpy as np
from numpy import *
import define
import kmeans

fi=xlrd.open_workbook('C:\Users\StMatengss\Desktop\mcm\data.xlsx')
sheet=fi.sheets()[0]
data=sheet.col_values(define.GRAD_DEBT_MDN10YR_SUPP)[1:]

counter=0

for x in data:
    if x=='PrivacySuppressed' or x=='NULL':counter=counter+1

print counter

print float(counter)/7804
