# -*- coding: utf-8 -*-
"""
Created on Sat May 21 13:20:18 2022

@author: sjtu
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

Narr=[5,10,20,50,80,100,120,150]
karr=[]
rN=10
mu=1.0
sigma=0.01
dt=0.0025

timeslice=np.arange(0,6,dt)
def f1(x, k, b):
    return k * x + b
def mcgen(N,rN,mu,sigma,timeslice):
    wavgarr=[]
    Tavgsm=np.zeros((len(timeslice),1))
    for  i in range(rN):
        x=np.zeros((N,1))
        w=np.ones((N,1))
        w=2*w
        Tavg=np.sum(1/w)/N
        tfirearr=np.zeros((N,1))
        tavgfire=np.sum(tfirearr)/N
        for t in timeslice:
            for jj in range(len(w)):
                Tavg=Tavg+1/w[jj]
            Tavg=Tavg/N
            for j in range(N):                
                x[j]=x[j]+w[j]*dt
                if x[j]>=1.:
                    x[j]=0.
                    if t<2*dt:
                        nextw=1/Tavg
                        w[j]=nextw
                        tfirearr[j]=t
                    else:
                        nextw=1/(Tavg+tavgfire+Tavg-t)
                        w[j]=np.random.normal(loc=mu, scale=sigma, size=None)+nextw 
                        #if w[j]>4:
                        #   w[j]=4
                        if w[j]<0:
                            w[j]=0
                        tfirearr[j]=t
            tavgfire=np.sum(tfirearr)/N
            
            wavg=np.mean(w)
            wavgarr.append(wavg)
        for ii in range(len(wavgarr)):
            Tavgsm[ii]=Tavgsm[ii]+wavgarr[ii]
        wavgarr.clear()
    Tavgsm=Tavgsm/rN
    timeslicefit=np.array(timeslice[10:400]).flatten() 
    Tavgsmfit=np.array(Tavgsm[10:400]).flatten()
    k1, b1 = optimize.curve_fit(f1, timeslicefit, Tavgsmfit)[0]
    return k1,Tavgsm
for n in range(len(Narr)):
    k0,Tavgsm0=mcgen(Narr[n], rN, mu, sigma, timeslice)
    karr.append(k0)
plt.plot(Narr, karr,'o-')
plt.xlabel('N')
plt.ylabel('Frequency slope (Hz/s)')
plt.savefig('accM1N.png')