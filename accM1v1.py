# -*- coding: utf-8 -*-
"""
Created on Sat May 21 13:20:18 2022

@author: sjtu
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

N=10
rN=10
mu=[0,0.1,0.5,1.0,1.5]
sigma=[0.01,0.1,1]
dt=0.0025

timeslice=np.arange(0,8,dt)
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
k0,Tavgsm0=mcgen(N, rN, mu[0], sigma[0], timeslice)
k1,Tavgsm1=mcgen(N, rN, mu[1], sigma[0], timeslice)
k2,Tavgsm2=mcgen(N, rN, mu[2], sigma[0], timeslice)
k3,Tavgsm3=mcgen(N, rN, mu[3], sigma[0], timeslice)
k4,Tavgsm4=mcgen(N, rN, mu[4], sigma[0], timeslice)
print(k0,k1,k2,k3,k4)
plt.plot(timeslice, Tavgsm0, label=chr(956)+'=0')
plt.plot(timeslice, Tavgsm1, label=chr(956)+'=0.1')
plt.plot(timeslice, Tavgsm2, label=chr(956)+'=0.5')
plt.plot(timeslice, Tavgsm3, label=chr(956)+'=1.0')
plt.plot(timeslice, Tavgsm4, label=chr(956)+'=2.0')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.legend(loc='right')
plt.savefig('accM1.png')