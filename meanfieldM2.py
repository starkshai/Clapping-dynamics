# -*- coding: utf-8 -*-
"""
Created on Tue May 17 21:47:56 2022

@author: sjtu
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.integrate import odeint

expstartarr=[]
expstarttimearr=[]
N=20
with open("expstart.txt", "r") as f1:
    expstart=f1.readline()
    expstartarr.append(float(expstart))
    expstarttime=f1.readline()
    expstarttimearr.append(float(expstarttime))
    while expstart and expstarttime:
        expstart=f1.readline()
        if expstart != '':
            expstartarr.append(float(expstart))
        expstarttime=f1.readline()
        if expstarttime != '':
            expstarttimearr.append(float(expstarttime))
    f1.close()
expstartout=np.array(expstartarr)
expstartTout=np.array(expstarttimearr)
dy=np.sqrt(expstartout/N)
dyu=[]
for i in range(len(dy)):
    if dy[i]+expstartout[i]>1:
        tmp=1-expstartout[i]
        dyu.append(tmp)
    else:
        dyu.append(dy[i])
err_range=[dy,dyu]
def fitfunc(t, lamb2):
    'Function that returns Ca computed from an ODE for a k'
    def ode1(s, t):
        return N * lamb2 * s * (1-s)

    s0 = expstartout[0]
    ssol = odeint(ode1, s0, t)
    return ssol[:,0]
lamb2_fit, lamb1cov = curve_fit(fitfunc, expstartTout, expstartout, p0=0.1)
perr = np.sqrt(np.diag(lamb1cov))
print(lamb2_fit,perr)
tfit = np.linspace(0,int(expstartTout[-1])+1);
fit = fitfunc(tfit, lamb2_fit)
#plt.plot(expstarttimearr, expstartarr, 'ro', label='data')
plt.errorbar(expstarttimearr,expstartarr,yerr=err_range,fmt='o',ecolor='r',color='k',elinewidth=2,capsize=4,label='data')
plt.plot(tfit, fit, 'b-', label='fit')
plt.legend(loc='best')
plt.savefig('M2fit.png')