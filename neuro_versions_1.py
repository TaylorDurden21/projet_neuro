# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 09:13:06 2018

@author: luna6
"""

from copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from math import sqrt
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')


data = pd.read_csv('C:/Users/luna6/Desktop/proje_neuro/test2.csv')
print("Input Data and Shape")
print(data.shape)
data.head()



print("Liste des colonnes : \n")
for row in data:
    print(row)

# Getting the values and plotting it
f1 = data['V1'].values
f2 = data['V2'].values
X = np.array(list(zip(f1, f2)))

plt.scatter(f1, f2, c='blue', s=7)

print(X[1])
print(X[1][0])
print(X[2])
print(np.linalg.norm(X[2] - X[1],2))

x1=X[1][0]
y1=X[1][1]
x2=X[2][0]
y2=X[2][1]
d=sqrt((x1-x2)**2 + (y1-y2)**2)
print("A la main",d)



baba=[]
tata=[[1,3],[56,45]]
#tata.index([56,45])
tata[0]
baba.append(tata[1])
print(baba)
baba.append(tata[0])
print(baba)

def distance_point(Tabs,point): #Prend en entrée un point et cacule la distance en le tableaux de vecteur et le points
    result=[]
    for i in range(len(Tabs)) :
        d=sqrt((Tabs[i][0]-point[0])**2 + (Tabs[i][1]-point[1])**2)
        result.append(d)
    return(result);


        
def regroupement(Tabs,centres):
    result=[]
    
    #----Calcul des distances en les centres et l'ensemble des points---
    d1=[]
    d2=[]
    d3=[]
    g1=[]
    g2=[]
    g3=[]
    #On prend la valeur de chaque centre
    centre1=[centres[0][0], centres[0][1]]
    centre2=[centres[1][0], centres[1][1]]
    centre3=[centres[2][0], centres[2][1]]
    
    d1=distance_point(Tabs,centre1)
    d2=distance_point(Tabs,centre2)
    d3=distance_point(Tabs,centre3)
    
    for i in range(len(d1)) :
        tab=[d1[i],d2[i],d3[i]]
        m=tab.index(min(tab))
        if m == 0 :
            g1.append(Tabs[i])
        elif m == 1:
             g2.append(Tabs[i])
        elif m == 2 :
            g3.append(Tabs[i])
            
    result=[g1,g2,g3]
    return(result);







def barycentre(group):
    Sx1=0
    Sy1=0
    
    Sx2=0
    Sy2=0
    
    Sx3=0
    Sy3=0
    
    result=[]
    g1=group[0]
    g2=group[1]
    g3=group[2]
    for i in range(len(g1)) :
        Sx1=(g1[i][0])+Sx1
        Sy1=(g1[i][1])+Sy1
        
    for i in range(len(g2)) :
        Sx2=(g2[i][0])+Sx2
        Sy2=(g2[i][1])+Sy2
        
    for i in range(len(g3)) :
        
        Sx3=(g3[i][0])+Sx3
        Sy3=(g3[i][1])+Sy3
    
    Bx1=Sx1/(len(g1))
    By1=Sy1/(len(g1))
    
    Bx2=Sx2/(len(g2))
    By2=Sy2/(len(g2))
    
    Bx3=Sx3/(len(g3))
    By3=Sy3/(len(g3))
    
    
    
    result.append([Bx1,By1])
    result.append([Bx2,By2])
    result.append([Bx3,By3])
    
    return(result);
    
    


print("--------- Zone de test ------")
papa=[[9,0],[10,2],[0,1]]
v=regroupement(X,papa)
#print(v[2])
gr=v[2]
print(gr[4])
print(gr[4][0])
print(gr[4][1])
print(papa)
bb=barycentre(v)
print(bb)

print('\n \n \n----------------------test de K-means-----------------------------\n')
#Si le barycentre de sortie est le même que en entré on arréte


papa=[[10,0],[10,2],[10,1]]
tmp1=papa
tmp2=[]
while(np.array_equal(tmp1,tmp2) == False) :
    tmp2=tmp1
    group=regroupement(X,tmp1)
    tmp1=barycentre(group)
  

print(tmp1)
print('tu es con')
if(np.array_equal(tmp1,tmp2)== True):
    print('Fin du programme')
    
bary1=tmp1[0]
bary2=tmp1[1]
bary3=tmp1[2]



plt.scatter(bary1[0],bary1[1], marker='*', s=200, c='g')    
plt.scatter(bary2[0],bary2[1], marker='^', s=200, c='r')    
plt.scatter(bary3[0],bary3[1], marker='h', s=200, c='b')

g1=group[0]
g2=group[1]
g3=group[2]

for i in range(len(g1)):
    plt.scatter(g1[i][0],g1[i][1], marker='*', s=10, c='r')
    
for i in range(len(g2)):
    plt.scatter(g2[i][0],g2[i][1], marker='*', s=10, c='b')
    
for i in range(len(g3)):
    plt.scatter(g3[i][0],g3[i][1], marker='*', s=10, c='m')    

plt.scatter(bary1[0],bary1[1], marker='*', s=200, c='g')    
plt.scatter(bary2[0],bary2[1], marker='^', s=200, c='r')    
plt.scatter(bary3[0],bary3[1], marker='h', s=200, c='b')

print('tu es con')




