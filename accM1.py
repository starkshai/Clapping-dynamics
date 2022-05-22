# -*- coding: utf-8 -*-
"""
Created on Sat May 21 13:20:18 2022

@author: sjtu
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

N=1
rN=1
mu=1.0
sigma=0.01
dt=0.0025

timeslice=np.arange(0,10,dt)
wavgarr=[]

Tavgsm=np.zeros((len(timeslice),1))

for  i in range(rN):
    if i%10 == 0:
        print("round ", i)
    x=np.zeros((N,1))
    w=np.ones((N,1))
    w=2*w
    Tavg=np.sum(1/w)/N
    tfirearr=np.zeros((N,1))
    tavgfire=np.sum(tfirearr)/N
    for t in timeslice:
        for j in range(N):                
            x[j]=x[j]+w[j]*dt
            if x[j]>=1.:
                x[j]=0.
                for jj in range(len(w)):
                    Tavg=Tavg+1/w[jj]
                Tavg=Tavg/N
                if t<2*dt:
                    nextw=2
                    w[j]=nextw
                    tfirearr[j]=t
                else:
                    nextw=1/(2*Tavg+tavgfire-t)
                    w[j]=np.random.normal(loc=mu, scale=sigma, size=None)+nextw  
                    #if w[j]>4:
                     #   w[j]=4
                    if w[j]<0:
                        w[j]=0
                    tfirearr[j]=t
                    #print(t,x[j],w[j])
        #print(t,x[j],w[j],Tavg,tavgfire)
        tavgfire=np.sum(tfirearr)/N   
        wavg=np.mean(w)
        wavgarr.append(wavg)
    for ii in range(len(wavgarr)):
        Tavgsm[ii]=Tavgsm[ii]+wavgarr[ii]
    wavgarr.clear()
Tavgsm=Tavgsm/rN
def f1(x, k, b):
    return k * x + b
timeslicefit=np.array(timeslice[10:500]).flatten() 
Tavgsmfit=np.array(Tavgsm[10:500]).flatten()
k1, b1 = optimize.curve_fit(f1, timeslicefit, Tavgsmfit)[0]
y1 = k1 * timeslicefit + b1
plt.plot(timeslice, Tavgsm, 'b-', label='data')
plt.plot(timeslicefit, y1, 'r.',label='fit')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.legend(loc='best')
plt.savefig('accM1.png')

