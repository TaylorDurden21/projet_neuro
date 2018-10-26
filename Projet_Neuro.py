# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 19:36:42 2018
@author: User
"""

7
#load data and libraries
import numpy as np
import pandas as pd
import csv as csv
import statsmodels.api as sm
import statsmodels.formula.api as smf


mydata = pd.read_csv("C:/Users/luna6/Desktop/proje_neuro/googleplaystore.csv", index_col=0)

#alternatively
#graphical representation
import matplotlib.pyplot as plt
x= mydata.Rating
y = mydata.Reviews
print("La taille de x est")
x2=[O for i in range(len(x))]

for i in range(len(x)) :
    x2[i]=x[i]


print(x2[45])




#plt.plot (x,y,'r+') #for each x and y pair
#
#
##plt.xlabel('Rating')
##plt.ylabel('Reviews')
##plt.title('Nuage de points')
##plt.scatter(x,y)
##print(';;;;;;;;;;;;;;;;;;hello world!!!!!!!!!!!!!')
##plt.show()
##print('hello world!!!!!!!!!!!!!')
#
##problémes sur le tableaux 