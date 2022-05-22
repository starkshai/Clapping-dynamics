# -*- coding: utf-8 -*-
"""
Created on Tue May 17 21:47:56 2022

@author: sjtu
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.integrate import odeint
import math

expstoparr=[]
expstoptimearr=[]
N=20
lamb=7.13371381e-02
t0=0.3613333333333334
ss0=0.014925373134328358
c=math.exp(lamb*N*t0)*(1/ss0-1)
with open("expstop.txt", "r") as f1:
    expstop=f1.readline()
    expstoparr.append(float(expstop))
    expstoptime=f1.readline()
    expstoptimearr.append(float(expstoptime))
    while expstop and expstoptime:
        expstop=f1.readline()
        if expstop != '':
            expstoparr.append(float(expstop))
        expstoptime=f1.readline()
        if expstoptime != '':
            expstoptimearr.append(float(expstoptime))
    f1.close()
expstopout=np.array(expstoparr)
expstopTout=np.array(expstoptimearr)
dy=np.sqrt(expstopout/N)
dyu=[]
for i in range(len(dy)):
    if dy[i]+expstopout[i]>1:
        tmp=1-expstopout[i]
        dyu.append(tmp)
    else:
        dyu.append(dy[i])
err_range=[dy,dyu]
def fitfunc(t,g1,g2):
    def ode1(s, t):
        return g1*(math.exp(N*lamb*t)/(math.exp(N*lamb*t)+c)-s)+g2*N*s*(math.exp(N*lamb*t)/(math.exp(N*lamb*t)+c)-s)
    s0 = 0
    ssol = odeint(ode1, s0, t)
    return ssol[:,0]
lamb_fit, lambcov = curve_fit(fitfunc, expstopTout, expstopout,p0=[0.001,0.0001],bounds=(0, [10.,10.]))
perr = np.sqrt(np.diag(lambcov))
print(lamb_fit)
print(perr)
tfit = np.linspace(0,int(expstopTout[-1])+1);
fit = fitfunc(tfit, lamb_fit[0],lamb_fit[1])
plt.errorbar(expstoptimearr,expstoparr,yerr=err_range,fmt='o',ecolor='r',color='k',elinewidth=2,capsize=4,label='data')
plt.plot(tfit, fit, 'b-', label='fit')
plt.legend(loc='best')
plt.savefig('Mstopfit.png')