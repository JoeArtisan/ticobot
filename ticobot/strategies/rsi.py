#!/usr/bin/python
import numpy as np

class Rsi:
    def __init__(self,prices,period,overhigh,overlow):
        self.prices = prices
        self.period = period
        self.overhigh = overhigh
        self.overlow = overlow
    
    def prepare(self):
        a = self.prices
        b = self.period
        return a,b,np.zeros(len(a)),np.zeros(len(a)),np.zeros(len(a)),np.zeros(len(a)),np.zeros(len(a)),np.zeros(len(a))
        
    def getSignal(self):
        a,b,change,gain,loss,ag,al,result = self.prepare()

        for i in range(1,len(a)):
            change[i] = a[i]-a[i-1]
            if change[i] == 0:
                gain[i] = 0
                loss[i] = 0
            if change[i] < 0:
                gain[i] = 0
                loss[i] = np.fabs(change[i])
            if change[i] > 0:
                gain[i] = change[i]
                loss[i] = 0

        ag[b] = np.sum(gain[1:b+1])/b# initial average gain
        al[b] = np.sum(loss[1:b+1])/b# initial average loss

        for i in range(b+1,len(a)):
            ag[i] = (ag[i-1]*(b-1)+gain[i])/b
            al[i] = (al[i-1]*(b-1)+loss[i])/b
        for i in range(b,len(a)):
            result[i] = 100-100/(1+ag[i]/al[i])
            
        rsi = result[b:]
        rsi = rsi[-1]

        return 'call' if rsi < self.overlow else 'put' if rsi > self.overhigh else 'ntr'
