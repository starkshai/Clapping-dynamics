# -*- coding: utf-8 -*-
"""
Created on Wed May 18 12:29:39 2022

@author: sjtu
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy import random

lamb1=1.45094592e-01
lamb2=2.04372131e-02
lamb3=5.07890868e-17

lamb22=7.13371381e-02
lamb33=3.21085908e-26
g1=0.12235982
g2=0.02209517
Ni=20
tot=10000
startT=[]
timera = np.arange(0, 15, 0.1)
stopT=[]
for simnumb in range(tot):
    S=Ni-1
    I=1
    R=0
    S0=S
    nextT=0
    startT.append(0)
    for ii in range(S0):
        p=lamb22*(1-S/Ni)*S+lamb33*(1-S/Ni)*(1-S/Ni)*S
        nextT=random.exponential(p)+nextT
        startT.append(nextT)
        S=S-1
    jpoint=1
    for j in range(len(timera)-1):
        if timera[j]<=startT[jpoint-1]:
            di=0
            pp = random.random()
            ptmp=g1+g2*R
            if pp < random.exponential(ptmp) and I>0:
                di = di+1
                stopT.append(timera[j])
            else:
                di=0
            I=I-di
            R=R+di
        elif jpoint<len(startT):
            I=I+1
            jpoint=jpoint+1
        else:
            di=0
            pp = random.random()
            ptmp=g1+g2*R
            if pp < random.exponential(ptmp) and I>0:
                di = di+1
                stopT.append(timera[j])
            else:
                di=0
            I=I-di
            R=R+di
startTarr=[]
for i in range(len(startT)):
    if startT[i]<10:
        startTarr.append(startT[i])
stopTarr=[]
for i in range(len(stopT)):
    if startT[i]<15:
        stopTarr.append(stopT[i])       
        
startT1=[]

for simnumb in range(tot):
    S=Ni-1
    I=1
    R=0
    S0=S
    nextT=0
    startT1.append(0)
    for ii in range(S0):
        p=lamb1+lamb2*(1-S/Ni)*S+lamb3*(1-S/Ni)*(1-S/Ni)*S
        nextT=random.exponential(p)+nextT
        startT1.append(nextT)
        S=S-1

startTarr=[]
for i in range(len(startT)):
    if startT[i]<12:
        startTarr.append(startT[i])
startTarr1=[]
for i in range(len(startT1)):
    if startT1[i]<12:
        startTarr1.append(startT1[i])
fig, ax = plt.subplots(figsize=(8, 4))
bn,bbins,bpatches=ax.hist(startTarr,30,density=True, histtype='step',cumulative=True, label='started clapping with M2M3')
ax.hist(startTarr1,30,density=True, histtype='step',cumulative=True, label='started clapping with M1M2M3')
ax.hist(stopTarr,30,density=True, histtype='step',cumulative=True, label='stopped clapping')

ax.set_xlabel('Time (s)',size=15)
ax.set_ylabel('Proportion of individuals',size=15)
ax.legend(loc='right',prop={"family": "Times New Roman", "size": 15})
plt.savefig("mcstartplot.png")
plt.show()