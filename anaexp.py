# -*- coding: utf-8 -*-
"""
Created on Tue May 17 12:14:38 2022

@author: sjtu
"""
import matplotlib.pyplot as plt
import numpy as np

startarr=[]
stoparr=[]
claparr=[]
x_time=[]
durationarr=[]
evtnumb=0
startflag=0
rawnumb=0
with open("./ExpData/inID.txt", "r") as f1:
    with open("./ExpData/TimeData.txt", "r") as f2:
        pID=f1.readline()
        pID_pre=pID
        startflag=1
        evtnumb=evtnumb+1
        timedata=f2.readline()
        timedata_pre=timedata
        starttime=timedata
        startarr.append(float(starttime))
        pID=f1.readline()
        timedata=f2.readline()
        while pID and timedata:
            rawnumb=rawnumb+1
            if pID != pID_pre:
                evtnumb=evtnumb+1
                if timedata != 'NA\n' and timedata != '\n':
                    if startflag==1:
                        stoptime=timedata_pre
                        stoparr.append(float(stoptime))
                        startflag=0
                        duration=float(stoptime)-float(starttime)
                        if duration<0.5:
                            print('%d',duration)
                            print(rawnumb)
                            print("id is "+pID)
                        durationarr.append(duration)
                    starttime=timedata
                    startarr.append(float(starttime))
                    startflag=1
                    pID_pre=pID
                    pID=f1.readline()
                    timedata_pre=timedata
                    timedata=f2.readline()
                else :
                    if startflag==1:
                        stoptime=timedata_pre
                        stoparr.append(float(stoptime))
                        startflag=0
                        duration=float(stoptime)-float(starttime)
                        durationarr.append(duration)
                    pID_pre=pID
                    pID=f1.readline()
                    timedata_pre=timedata
                    timedata=f2.readline()
            else :
                pID=f1.readline()
                timedata_pre=timedata
                timedata=f2.readline()
        if startflag==1:
            stoptime=timedata_pre
            stoparr.append(float(stoptime))
            startflag=0
            duration=float(stoptime)-float(starttime)
            durationarr.append(duration)
        f2.close()
    f1.close()

print("total events number is "+str(evtnumb))

durout=np.array(durationarr)
durmean=np.mean(durout)
durstd=np.std(durout)
durstr='mean='+str(round(durmean,2))+'; std='+str(round(durstd,2))

plt.figure()
y,binEdges =np.histogram(durationarr,bins=20)
bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
menStd     = np.sqrt(y)
width      = 0.5
plt.bar(bincenters, y, width=width, color='r', yerr=menStd)
plt.xlabel('Time (s)',size=15)
plt.ylabel('Counts',size=15)
plt.text(0,25,durstr, size=15)
plt.savefig("expduration.png")
plt.show()

#yb,bbinEdges=np.histogram(startarr,bins=20)
#ye,ebinEdges=np.histogram(stoparr,bins=20)
plt.figure()
fig, ax = plt.subplots(figsize=(8, 4))
bn,bbins,bpatches=ax.hist(startarr,30,density=True, histtype='step',cumulative=True, label='started clapping')
en,ebins,epatches=ax.hist(stoparr,30,density=True,histtype='step',cumulative=True, label='stopped clapping')
ax.set_xlabel('Time (s)',size=15)
ax.set_ylabel('Proportion of individuals',size=15)
ax.legend(loc='right',prop={"family": "Times New Roman", "size": 15})
plt.savefig("exrplot.png")
plt.show()
f3=open('expstart.txt',mode='w')
for i in range(len(bn)):
    f3.writelines(str(bn[i])+'\n')
    f3.writelines(str((bbins[i]+bbins[i+1])/2)+'\n')
f3.close()
f4=open('expstop.txt',mode='w')
for i in range(len(en)):
    f4.writelines(str(en[i])+'\n')
    f4.writelines(str((ebins[i]+ebins[i+1])/2)+'\n')
f4.close()