#!/usr/bin/python
import numpy as np

class Rsi:
    def __init__(self,prices,period,overhigh,overlow):
        self.prices = prices
        self.period = period
        self.overhigh = overhigh
        self.overlow = overlow
        
    def getSignal(self):
        a = self.prices
        b = self.period
        change = np.zeros(len(a))
        gain = np.zeros(len(a))
        loss = np.zeros(len(a))
        ag = np.zeros(len(a))
        al = np.zeros(len(a))
        result = np.zeros(len(a))
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
        print(f'Ticobot: Fuerza Relativa: {rsi[-1]}')
        return 'call' if rsi[-1] < self.overlow else 'put' if rsi[-1] > self.overhigh else 'ntr'
