from numpy import *
import numpy as np
import math
import matplotlib.pyplot as plt

DIM=2
NUMSAPLES=100
TIMES=10
INF=1e9
mark1 = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
mark2 = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']  

def caldis(v1,v2,maxvalue):
    return sqrt(sum(power(v1-v2,2)/maxvalue))

def initcenter(data,k):
    numSamples,dim=data.shape
    centers=zeros((k,dim))
    for i in range(k):
        index=int(random.uniform(0,numSamples))
        centers[i,:]=data[index,:]
    return centers

def drawpic(data,k,centers,clusters,xs,ys):
    numSamples,dim=data.shape
    if dim==2:
        for i in range(numSamples):
            plt.plot(data[i,0],data[i,1],mark1[clusters[i]])
        for i in range(k):
            plt.plot(centers[i,0],centers[i,1],mark2[i],markersize=12)
        plt.xlabel(xs)
        plt.ylabel(ys)
        plt.show()
        plt.savefig(xs+'-'+ys+'.png')

def savefile(data,k,centers,clusters,clusterNum,name):
    st=''
    for i in name:
        st=st+i+'-'
    np.savetxt(st+'data.txt',data)
    np.savetxt(st+'centers.txt',centers)
    np.savetxt(st+'clusterNum.txt',array(clusterNum),fmt='%d')
    np.savetxt(st+'clusters.txt',array(clusters),fmt='%d')

def kmeans(data,k,name):
    numSamples,dim=data.shape

    xs=name[0]
    ys=name[1]
    clusters=[0]*numSamples
    clusterflag=True
    clusterNum=[0]*k
    maxvalue=np.max(data,axis=0)
    centers=initcenter(data,k)
    print maxvalue
    for t in range(TIMES):
        for i in range(numSamples):
            minDis=INF
            minIndex=0
            for j in range(k):
                dis=caldis(centers[j,:],data[i,:],maxvalue)
                if dis<minDis:
                    minDis=dis
                    minIndex=j
            clusters[i]=minIndex

        for i in range(k):
            tmp=[]
            for n,j in enumerate(clusters):
                if j==i:
                    tmp.append(data[n,:])
            centers[i,:]=mean(array(tmp),axis=0)
    for i in range(k):
        for n,j in enumerate(clusters):
            if j==i:
                clusterNum[i]=clusterNum[i]+1
    savefile(data,k,centers,clusters,clusterNum,name)
    drawpic(data,k,centers,clusters,xs,ys)
    return centers,clusters


               
#print kmeans(array([[1,2,3],[2,4,3],[4,5,6],[1,2,7],[4,6,1]],dtype=float),2,['',''])

    
