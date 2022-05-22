# -*- coding: utf-8 -*-
"""
Created on Wed May 18 12:29:39 2022

@author: sjtu
"""
import numpy as np
import matplotlib.pyplot as plt
import random

lamb2=7.13371381e-02
lamb3=3.21085908e-26
g1=0.12235982
g2=0.02209517
Ni=2510
tot=10000
Sarr=[]
Iarr=[]
Rarr=[]
S,I,R=tot-1,1,0
time = np.arange(0, 15, 0.01)
for simnumb in time:
    Sarr.append(S)
    Iarr.append(I)
    Rarr.append(R)
    ds,di=0,0
    for n in range(S):
        p = random.random()
        sr=I/Ni
        ptmp=lamb2*sr+lamb3*sr*sr
        if p < ptmp:
            ds += 1
    S-=ds
    for n in range(I):
        p = random.random()
        rr=R/Ni
        ptmp=g1+g2*rr
        if p < ptmp:
            di += 1
    I=I+ds-di
    R+=di
plt.plot(time,Sarr, linestyle='-', color='red', label='number of S')
plt.plot(time,Iarr, linestyle='-', color='blue', label='number of I')
plt.plot(time,Rarr, linestyle='-', color='green', label='number of R')
plt.legend()
plt.xlabel('t', fontsize=14)
plt.ylabel('counts', fontsize=14)
plt.show()