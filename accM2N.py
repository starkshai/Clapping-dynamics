# -*- coding: utf-8 -*-
"""
Created on Sat May 21 13:20:18 2022

@author: sjtu
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

Narr=[5,10,20,50,80,100,120,150]
rN=10
mu=0
sigma=0.11
dt=0.0025
ep=0.2
karr=[]
timeslice=np.arange(0,10,dt)
def f1(x, k, b):
    return k * x + b
def f(x):
    if x>=0.5:
        return 1
    else:
        return -0.59
def mcgen(N,rN,mu,sigma,timeslice):
    wavgarr=[]
    Tavgsm=np.zeros((len(timeslice),1))
    for  i in range(rN):
        x=np.zeros((N,1))
        w=np.ones((N,1))
        w=2*w

        tfirearr=np.zeros((N,1))
        for t in timeslice:
            for j in range(N):                
                x[j]=x[j]+w[j]*dt
                if x[j]>=1.:
                    x[j]=0.
                    dw=1/(t-tfirearr[j])
                    w[j]=np.random.normal(loc=mu, scale=sigma, size=None)+dw 
                    tfirearr[j]=t
                    for jj in range(N):
                        if jj==j:
                            continue
                        else:
                            dxtmp=f(x[jj])*ep/N+x[jj]
                            if dxtmp>1:
                                x[jj]=1
                            elif dxtmp<0:
                                x[jj]=0
                            else:
                                x[jj]=dxtmp                              
            if w[j]>4:
                w[j]=4
            wavg=np.mean(w)
            wavgarr.append(wavg)
        for ii in range(len(wavgarr)):
            Tavgsm[ii]=Tavgsm[ii]+wavgarr[ii]
        wavgarr.clear()
    Tavgsm=Tavgsm/rN
    timeslicefit=np.array(timeslice[1000:4000]).flatten() 
    Tavgsmfit=np.array(Tavgsm[1000:4000]).flatten()
    k1, b1 = optimize.curve_fit(f1, timeslicefit, Tavgsmfit)[0]
    return k1,b1,Tavgsm,timeslicefit,Tavgsmfit
for n in range(len(Narr)):
    k0,b0,Tavgsm0,timeslicefit,Tavgsmfit=mcgen(Narr[n], rN, mu, sigma, timeslice)
    karr.append(k0)
plt.plot(Narr, karr,'o-')
plt.xlabel('N')
plt.ylabel('Frequency slope (Hz/s)')
plt.savefig('accM2N.png')